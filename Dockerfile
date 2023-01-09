# Use python version 3.11.1
FROM python:3.11.1

# Set the working directory to /usr/src/app (inside container)
WORKDIR /usr/src/app

# Copy all files to the container
COPY . .

# Upgrade pip
RUN pip install --upgrade pip
RUN pip install --upgrade wheel

# Install requirements
RUN pip install -r requirements.txt

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1
