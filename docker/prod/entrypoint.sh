#!/bin/bash
set -e

# Validate required environment variables
if [ -z "$WEBSOCKET_URI" ]; then
    echo "ERROR: WEBSOCKET_URI environment variable is not set"
    exit 1
fi

if [ -z "$BOOTSTRAP_SERVERS" ]; then
    echo "ERROR: BOOTSTRAP_SERVERS environment variable is not set"
    exit 1
fi

if [ -z "$BASE" ]; then
    echo "ERROR: BASE environment variable is not set"
    exit 1
fi

if [ -z "$QUOTE" ]; then
    echo "ERROR: QUOTE environment variable is not set"
    exit 1
fi

echo "Starting scrapper with:"
echo "  Websocket URI: $WEBSOCKET_URI"
echo "  Bootstrap Servers: $BOOTSTRAP_SERVERS"
echo "  Trading pair base: $BASE"
echo "  Trading pari quote: $QUOTE"

# Run the application
exec python -m scrapper.main
