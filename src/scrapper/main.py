import os
import asyncio
import json
import websockets
import time
from scrapper.settings import get_request
from scrapper.producer import producer


async def main():
    url = os.environ.get("WEBSOCKET_URI")

    # Measurement variables
    start_time = time.time()
    total_bytes = 0
    message_count = 0
    last_report_time = start_time

    async with websockets.connect(url) as websocket:
        request = get_request()
        await websocket.send(json.dumps(request))
        while True:
            try:
                data = await websocket.recv()

                # Calculate size in bytes
                data_size = len(data.encode("utf-8"))
                total_bytes += data_size
                message_count += 1

                # Display statistics every 10 seconds
                current_time = time.time()
                elapsed_since_last_report = current_time - last_report_time

                if elapsed_since_last_report >= 10 and os.environ.get("METRICS"):
                    total_elapsed = current_time - start_time
                    throughput_mb_s = (total_bytes / (1024 * 1024)) / total_elapsed

                    print(
                        f"[STATS] Throughput: {throughput_mb_s:.2f} MB/s | "
                        f"Messages: {message_count} | "
                        f"Total: {total_bytes / (1024 * 1024):.2f} MB | "
                        f"Time: {total_elapsed:.1f}s"
                    )

                    last_report_time = current_time

                # Display data
                if data.startswith("0"):
                    # Build topic from BASE and QUOTE environment variables.
                    base = os.environ.get("BASE", "").lower()
                    quote = os.environ.get("QUOTE", "").lower()
                    topic = f"raw-trades-{base}-{quote}"
                    producer.list_topics(topic)
                    producer.produce(
                        topic=topic,
                        value=data.encode("utf-8") if isinstance(data, str) else data,
                    )

                    # note: message_count is incremented earlier when data is received;
                    # avoid double-counting here.

                    if message_count % 1000 == 0:  # Flush every 1000 messages
                        producer.flush()

            except websockets.ConnectionClosed:
                break

    # Final report
    total_time = time.time() - start_time
    avg_throughput = (total_bytes / (1024 * 1024)) / total_time

    print(
        f"\n[FINAL] Average throughput: {avg_throughput:.2f} MB/s | "
        f"Messages received: {message_count} | "
        f"Total size: {total_bytes / (1024 * 1024):.2f} MB"
    )


if __name__ == "__main__":
    # Use asyncio.run() which is the modern, recommended API and avoids
    # DeprecationWarning about missing current event loop.
    asyncio.run(main())
