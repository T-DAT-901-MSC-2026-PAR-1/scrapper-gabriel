#!/bin/bash
set -e

# Ensure dependencies are installed in the venv
/usr/local/bin/uv sync --frozen

# Install the scrapper package in development mode
/usr/local/bin/uv pip install -e .

# Set PATH to use the venv
export PATH="/app/.venv/bin:$PATH"

# Run the application with auto-reload
watchmedo auto-restart --directory=./src --pattern='*.py' --recursive -- python -m scrapper.main
