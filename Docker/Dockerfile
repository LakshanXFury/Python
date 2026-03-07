# Use official Python image as base
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy files into the container
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Run the Python file
CMD ["python", "app.py"]


#1st command: docker build -t my-python-app .
  #
  #-t my-python-app gives your image a name
  #. means "use the Dockerfile in this current folder"

# 2nd command: docker run my-python-app