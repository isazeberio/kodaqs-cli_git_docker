# kodaqs-docker-illustration
# Version: 0.1.0
# Description: Dockerfile for illustration purposes in the KODAQS course
# Author: github.com/yfiua

# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Ensure the script is executable
RUN chmod +x /app/*.py

# Run the script by default when the container starts
CMD [ "sh", "-c", "./character-count.py cli.md" ]
