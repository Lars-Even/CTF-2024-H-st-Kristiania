FROM python:3-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Set the CMD using the JSON array syntax
CMD ["python3", "server.py"]  
