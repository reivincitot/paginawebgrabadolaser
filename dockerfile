FROM python:3.12-slim

# Set environment variables
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Command to run the application
CMD ["guinicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]