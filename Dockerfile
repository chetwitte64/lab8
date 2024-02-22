# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .
# Install SQLite 3
RUN apt-get update && apt-get install -y sqlite3
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn
# Copy the application code to the working directory
COPY . .

# Expose the port on which the Flask API will run
EXPOSE 5000

# Run create_sql.py here
RUN python create_sql.py

# Set the entrypoint command to run the Flask API
CMD gunicorn -b 0.0.0.0:5000 app:app --timeout 600
