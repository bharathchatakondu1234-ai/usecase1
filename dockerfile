# Use a tiny version of Python to keep the image small
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the web framework
RUN pip install flask

# Copy our app code into the container
COPY app.py .

# Expose port 80 to the cluster
EXPOSE 80

# Start the application
CMD ["python", "app.py"]
