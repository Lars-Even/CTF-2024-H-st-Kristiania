# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required Python packages
# RUN pip install -r requirements.txt   # Uncomment if you have a requirements file

# Expose the port the server listens on
EXPOSE 41111

# Run the Python script when the container launches
CMD ["python", "test.py"]
