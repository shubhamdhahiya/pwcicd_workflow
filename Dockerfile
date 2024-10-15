# Use an official Python runtime as a parent image
FROM python:3.12

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Set the working directory in the container
WORKDIR /app
#
# Copy the current directory contents into the container at /app
COPY . /app

# Copy requirements.txt to the container
COPY requirements.txt .

# List files in the /app directory to ensure requirements.txt is copied
RUN ls -l /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --verbose -r requirements.txt

# Define environment variables for BrowserStack credentials
ENV BROWSERSTACK_USERNAME=ankitsharma_5qd1B8
ENV BROWSERSTACK_ACCESS_KEY=ygXnpF6wGGoX8TZUqqDt

# Run your tests using pytest with BrowserStack SDK
CMD ["bash", "-c", "browserstack-sdk  pytest -v -k 'mark'"]
