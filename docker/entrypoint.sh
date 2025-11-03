#!/bin/bash
set -e

# Activate the virtual environment
source /app/.venv/bin/activate

# exec tail -f /dev/null
exec watchmedo auto-restart --directory=./src --pattern=*.py --recursive -- python src/main.py