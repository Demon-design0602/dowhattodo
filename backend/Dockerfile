# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV GEMINI_API_KEY=''

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "app:app"]

