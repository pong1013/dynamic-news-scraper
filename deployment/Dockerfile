## This is for linux/amd64 platform
# docker buildx build --platform linux/amd64 -t your-dockerhub-username/django-scrapy-app:1.0.1 .
# docker run --platform linux/amd64 -p 8000:8000 -p 6379:6379 pong1013/django-scrapy-nba:1.0.1

# Use Python base image with specific platform
FROM --platform=linux/amd64 python:3.9

# Install Redis
RUN apt-get update && apt-get install -y redis-server

# Set working directory
WORKDIR /app

# Copy only requirements first to leverage Docker cache
COPY udn_nba/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY udn_nba/ .

# Make start script executable
RUN chmod +x start.sh

# Create necessary directories if they don't exist
RUN mkdir -p static

# Expose ports for Django and Redis
EXPOSE 8000
EXPOSE 6379

# Set start command
CMD ["./start.sh"]