# Docker

## Introduction

Docker is a platform that allows you to create and run applications inside containers. Containers are lightweight, standalone, and executable packages that contain everything needed to run an application, including the code, runtime, system tools, libraries, and settings.
Using Docker can help you ensure that your research code runs consistently across different environments, or reproduce the results of other researchers by using their Docker images.

For example, in the previous session [Command line interface](cli.md) we used the Python to show case how to use the CLI to count the occurrence of characters A-Z in the file and plot a histogram of the character counts.
There are some shortcomings with this approach. Although we can run the Python script on our local machine, it may not run on another machine due to differences in the environment. For example, the script may not run on another machine or result in different output if the required Python packages are not installed, or if the Python version is different. Docker can help us solve this problem by creating a container that contains the Python script, the data, and all the required dependencies.

## Key concepts

### Images and containers

- **Image**: An image is a read-only template that contains the application code, runtime, libraries, dependencies, and other files needed to run an application. Images are used to create containers.

- **Container**: A container is a runtime instance of an image. It is a lightweight, standalone, and executable package that contains everything needed to run an application. Containers run in isolation from each other and from the host machine.

A container is a realisation of an image. You can think of an image as a class and a container as an object in the object oriented programming paradigm.
You can create multiple containers from the same image, and each container runs independently of the others.

### Dockerfile

A Dockerfile is a text file that contains a set of instructions for building a Docker image. The Dockerfile specifies the base image, working directory, dependencies, environment variables, and other configurations needed to create the image. You can imagine a Dockerfile as a recipe for building a Docker image.

## Installation

To install Docker on your machine, follow the instructions for your operating system on the official Docker website: <https://docs.docker.com/get-docker/>.

## Creating a simple Docker image

Now we will create a simple Docker image that runs the [Python script](characters-count.py) that we used in the previous session. The Python script reads a file and counts the occurrence of characters A-Z in the file, and then plots a histogram of the character counts.

Put the content below in a file named `Dockerfile` in the same directory as the Python script `character-count.py` and the requirements file `requirements.txt`.

```dockerfile
# kodaqs-docker-illustration
# Version: 0.1.0
# Description: Dockerfile for illustration purposes in the KODAQS course
# Author: github.com/yfiua

# Use the official Python base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Ensure the script is executable
RUN chmod +x /app/*.py

# Run the script by default when the container starts
CMD [ "sh", "-c", "./character-count.py cli.md" ]
```

The `Dockerfile` contains the following instructions:

- `FROM python:3.12-slim`: Use the official Python base image with Python 3.12, which is a lightweight version of Python that includes only the essentials.

- `WORKDIR /app`: Set the working directory in the container to `/app`.

- `COPY requirements.txt /app`: Copy the `requirements.txt` file from the host machine to the `/app` directory in the container.

- `RUN pip install -r requirements.txt`: Install the Python dependencies listed in the `requirements.txt` file.

- `COPY . /app`: Copy the contents of the current directory on the host machine to the `/app` directory in the container, which includes the Python script `character-count.py` and the data file `cli.md`.

- `RUN chmod +x /app/*.py`: Ensure that the Python script is executable.

- `CMD [ "sh", "-c", "./character-count.py cli.md" ]`: Run the Python script by default when the container starts, passing the `cli.md` file as an argument.

In principle it is also possible to construct the Docker image in a way that it can run the Python script with different files as input.
This can be done by mounting volumes when running the container.
However, for simplicity we will hard-code the file name in the `Dockerfile`.

## Building the Docker image

To build the Docker image, run the following command in the same directory as the `Dockerfile`:

```sh
docker build -t character-count .
```

This will build the Docker image with the tag `character-count`.

## Running the Docker container

To run the Docker container (strictly speaking, we run an instance of the Docker image as a container), run the following command:

```sh
docker run character-count
```

This will run the Python script inside the Docker container, which will read the `cli.md` file and count the occurence of characters A-Z in the file, and then plot a histogram of the character counts.

Run the following command to list the containers:

```sh
docker ps -a
```

The output of the script is displayed in the terminal. However, the plot file is saved in the container and not directly accessible from the host machine.
To retrieve the plot file, you can use the `docker cp` command to copy the file from the container to the host machine.

```sh
docker cp <container_id>:/app/character_count_histogram.png .
```

Replace `<container_id>` with the ID of our container.

## Docker Hub

Docker Hub <https://hub.docker.com> is a cloud-based registry service that allows you to share container images with others. You can use Docker Hub to store and manage your images, as well as to discover and use images created by others.

To push the Docker image to Docker Hub, you need to create an account on Docker Hub and log in using the `docker login` command in the terminal.

```sh
docker login
```


Then, you can tag the image with your Docker Hub username and push it to Docker Hub.

```sh
docker tag character-count <username>/character-count
docker push <username>/character-count
```

Replace `<username>` with your Docker Hub username.
After pushing the image to Docker Hub, it should appear in your personal Docker Hub profile <https://hub.docker.com/u/username>.
You can share the image with others by providing them with the image name and tag.

To use an image from Docker Hub, you can pull it using the `docker pull` command. Imagine that you are on another computer with Docker installed, but it does not necessarily have the Python environment set up.
To use the image that we just pushed to Docker Hub, you can pull it using the following command:

```sh
docker pull <username>/character-count
```

Then, you can run the Docker container using the pulled image:

```sh
docker run <username>/character-count
```

