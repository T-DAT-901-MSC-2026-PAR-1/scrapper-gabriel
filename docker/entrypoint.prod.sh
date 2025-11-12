#!/bin/bash
set -e

# Validate required environment variables
if [ -z "$BOOTSTRAP_SERVERS" ]; then
    echo "ERROR: BOOTSTRAP_SERVERS environment variable is not set"
    exit 1
fi

if [ -z "$KAFKA_USERNAME" ]; then
    echo "ERROR: KAFKA_USERNAME environment variable is not set"
    exit 1
fi

if [ -z "$KAFKA_PASSWORD" ]; then
    echo "ERROR: KAFKA_PASSWORD environment variable is not set"
    exit 1
fi

if [ -z "$WEBSOCKET_URI" ]; then
    echo "ERROR: WEBSOCKET_URI environment variable is not set"
    exit 1
fi

if [ -z "$KAFKA_TOPIC" ]; then
    echo "ERROR: KAFKA_TOPIC environment variable is not set"
    exit 1
fi

echo "Starting scrapper with:"
echo "  Bootstrap Servers: $BOOTSTRAP_SERVERS"
echo "  Kafka Username: $KAFKA_USERNAME"
echo "  Websocket URI: $WEBSOCKET_URI"
echo "  Kafka Topic: $KAFKA_TOPIC"

# Run the application
exec /app/.venv/bin/python -m scrapper.main
