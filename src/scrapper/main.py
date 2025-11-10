import asyncio
import json
import websockets
import time

REQUEST = {
    "action": "SubAdd",
    "subs": [
        "0~ABCC~BTC~USDT",
        "0~alphaex~BTC~USDT",
        "0~ascendex~BTC~USDT",
        "0~bequant~BTC~USDT",
        "0~Bgogo~BTC~USDT",
        "0~Bibox~BTC~USDT",
        "0~BigONE~BTC~USDT",
        "0~bilaxy~BTC~USDT",
        "0~Binance~BTC~USDT",
        "0~binanceusa~BTC~USDT",
        "0~bingx~BTC~USDT",
        "0~bit~BTC~USDT",
        "0~bit2me~BTC~USDT",
        "0~bitbns~BTC~USDT",
        "0~bitci~BTC~USDT",
        "0~BitexBook~BTC~USDT",
        "0~bitfex~BTC~USDT",
        "0~Bitfinex~BTC~USDT",
        "0~Bitforex~BTC~USDT",
        "0~bitget~BTC~USDT",
        "0~bithumbglobal~BTC~USDT",
        "0~BitMart~BTC~USDT",
        "0~Bitmex~BTC~USDT",
        "0~bitopro~BTC~USDT",
        "0~bitpanda~BTC~USDT",
        "0~bitrue~BTC~USDT",
        "0~Bitso~BTC~USDT",
        "0~Bitstamp~BTC~USDT",
        "0~BitTrex~BTC~USDT",
        "0~bitunix~BTC~USDT",
        "0~bkex~BTC~USDT",
        "0~Bleutrade~BTC~USDT",
        "0~blockchaincom~BTC~USDT",
        "0~BTCAlpha~BTC~USDT",
        "0~btcex~BTC~USDT",
        "0~BTCMarkets~BTC~USDT",
        "0~BTCTurk~BTC~USDT",
        "0~btse~BTC~USDT",
        "0~bullish~BTC~USDT",
        "0~bwexchange~BTC~USDT",
        "0~bybit~BTC~USDT",
        "0~bydfi~BTC~USDT",
        "0~Cexio~BTC~USDT",
        "0~Coinbase~BTC~USDT",
        "0~CoinDeal~BTC~USDT",
        "0~CoinEx~BTC~USDT",
        "0~CoinFalcon~BTC~USDT",
        "0~coinfield~BTC~USDT",
        "0~CoinJar~BTC~USDT",
        "0~Coinmate~BTC~USDT",
        "0~Coinsbit~BTC~USDT",
        "0~coinspro~BTC~USDT",
        "0~CoinTiger~BTC~USDT",
        "0~coinw~BTC~USDT",
        "0~coss~BTC~USDT",
        "0~crex24~BTC~USDT",
        "0~cryptodotcom~BTC~USDT",
        "0~cryptology~BTC~USDT",
        "0~Cryptopia~BTC~USDT",
        "0~currency~BTC~USDT",
        "0~deribit~BTC~USDT",
        "0~DigiFinex~BTC~USDT",
        "0~Exmo~BTC~USDT",
        "0~fastex~BTC~USDT",
        "0~FCoin~BTC~USDT",
        "0~flipster~BTC~USDT",
        "0~Foxbit~BTC~USDT",
        "0~ftx~BTC~USDT",
        "0~ftxus~BTC~USDT",
        "0~garantex~BTC~USDT",
        "0~Gateio~BTC~USDT",
        "0~Gemini~BTC~USDT",
        "0~Graviex~BTC~USDT",
        "0~hashkey~BTC~USDT",
        "0~HitBTC~BTC~USDT",
        "0~HuobiPro~BTC~USDT",
        "0~indodax~BTC~USDT",
        "0~indoex~BTC~USDT",
        "0~Kraken~BTC~USDT",
        "0~Kucoin~BTC~USDT",
        "0~Kuna~BTC~USDT",
        "0~LAToken~BTC~USDT",
        "0~LBank~BTC~USDT",
        "0~Liqnet~BTC~USDT",
        "0~Liquid~BTC~USDT",
        "0~Luno~BTC~USDT",
        "0~Lykke~BTC~USDT",
        "0~MercadoBitcoin~BTC~USDT",
        "0~mercatox~BTC~USDT",
        "0~mexc~BTC~USDT",
        "0~mock~BTC~USDT",
        "0~nominex~BTC~USDT",
        "0~OKCoin~BTC~USDT",
        "0~OKEX~BTC~USDT",
        "0~onetrading~BTC~USDT",
        "0~osl~BTC~USDT",
        "0~P2PB2B~BTC~USDT",
        "0~paramountdax~BTC~USDT",
        "0~paribu~BTC~USDT",
        "0~phemex~BTC~USDT",
        "0~Poloniex~BTC~USDT",
        "0~probit~BTC~USDT",
        "0~safetrade~BTC~USDT",
        "0~sigenpro~BTC~USDT",
        "0~TheRockTrading~BTC~USDT",
        "0~timex~BTC~USDT",
        "0~Tokenomy~BTC~USDT",
        "0~toobit~BTC~USDT",
        "0~tradeogre~BTC~USDT",
        "0~Unocoin~BTC~USDT",
        "0~Upbit~BTC~USDT",
        "0~valr~BTC~USDT",
        "0~vitex~BTC~USDT",
        "0~wazirx~BTC~USDT",
        "0~whitebit~BTC~USDT",
        "0~woo~BTC~USDT",
        "0~xcoex~BTC~USDT",
        "0~xtpub~BTC~USDT",
        "0~yellow~BTC~USDT",
        "0~Yobit~BTC~USDT",
        "0~zbdotcom~BTC~USDT",
        "0~ZBG~BTC~USDT",
        "0~zebitex~BTC~USDT",
        "0~zonda~BTC~USDT",
    ],
}


async def main():
    url = "wss://streamer.cryptocompare.com/v2?format=streamer"

    # Measurement variables
    start_time = time.time()
    total_bytes = 0
    message_count = 0
    last_report_time = start_time

    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps(REQUEST))
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

                if elapsed_since_last_report >= 10:
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
                # if data.startswith('0'):
                # print(data)

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
    asyncio.get_event_loop().run_until_complete(main())
