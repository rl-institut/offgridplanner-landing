FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install deps from lockfile
RUN uv sync --locked

# Copy app files
COPY . .

# Expose port
EXPOSE 5000

# Run with Gunicorn
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]