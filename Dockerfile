# Use the official Python image from Docker Hub
FROM python:3.13-slim

# Install dependencies including PostgreSQL development libraries (required for psycopg2-binary)
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 for the app
EXPOSE 5000

# Define the command to run the application
CMD ["python", "run.py"]
