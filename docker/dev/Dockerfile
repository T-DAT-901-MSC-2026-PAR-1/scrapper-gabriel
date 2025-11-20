FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app

# Install system dependencies for Jupyter
RUN apt-get update && apt-get install -y --no-install-recommends \
    tini \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Create virtual environment and install dependencies
RUN uv sync --frozen

# Make entrypoint script executable
RUN chmod +x /app/docker/dev/entrypoint.sh

# Use tini to handle signals properly
ENTRYPOINT ["/usr/bin/tini", "--", "/bin/bash", "/app/docker/dev/entrypoint.sh"]
