# Use the official Python image from Docker Hub
FROM python:3.13-slim

# Install system dependencies including PostgreSQL dev libraries
RUN apt-get update && \
    apt-get install -y libpq-dev curl && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Download and set permissions for wait-for-it.sh
RUN curl -o /app/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /app/wait-for-it.sh

# Expose Flask default port
EXPOSE 5000