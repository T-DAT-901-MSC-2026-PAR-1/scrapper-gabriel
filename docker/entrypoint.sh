#!/bin/bash
set -e

# Set PATH and PYTHONPATH for the virtual environment
export PATH="/app/.venv/bin:$PATH"
export PYTHONPATH="/app/.venv/lib/python3.13/site-packages:$PYTHONPATH"

# exec tail -f /dev/null
exec watchmedo auto-restart --directory=./src --pattern=*.py --recursive -- python src/main.py