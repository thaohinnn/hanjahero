# Use the official Python image from the Docker Hub.
FROM python:3.9-slim

# Set environment variables.
ENV PYTHONUNBUFFERED=1

# Create and set the working directory.
RUN mkdir /app
WORKDIR /app

# Install system dependencies.
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-venv \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment.
RUN python3 -m venv /opt/venv

# Ensure venv is used for subsequent commands.
ENV PATH="/opt/venv/bin:$PATH"

# Install Python dependencies.
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Install Gunicorn
RUN pip install gunicorn
# Expose the port that Gunicorn will run on.
EXPOSE 8000
# Set PYTHONPATH
ENV DJANGO_SETTINGS_MODULE=hanjahero.settings
ENV PYTHONPATH="/app:/app/home:${PYTHONPATH}"
# Run database migrations and start the Gunicorn server.
CMD ["sh", "-c", "gunicorn hanjahero.wsgi:application --bind 0.0.0.0:8000"]
