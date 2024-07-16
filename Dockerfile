# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Django and psycopg2 (PostgreSQL adapter for Python)
RUN pip install django psycopg2-binary

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]