# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
