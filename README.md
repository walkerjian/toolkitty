
# Network Diagnostics Project

This project is designed to perform network diagnostics, including retrieving the local IP address, checking HTTPS connectivity, performing traceroute, and geolocating IP addresses. The project is containerized using Docker and can be run in a Jupyter Notebook environment for interactive development.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Docker Container](#run-the-docker-container)
- [Using Jupyter Notebook](#using-jupyter-notebook)
- [Project Structure](#project-structure)
- [Functions Overview](#functions-overview)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Docker and Docker Compose installed on your system.
- Git installed on your system.
- A GitHub account for repository management.

## Setup

### Clone the Repository

First, clone the repository from GitHub:

```sh
git clone https://github.com/yourusername/network_diagnostics.git
cd network_diagnostics
```

### Build the Docker Image

Build the Docker image to ensure all dependencies are installed:

```sh
docker-compose build
```

### Run the Docker Container

Start the Docker container with the following command:

```sh
docker-compose up
```

To run the container in the background, use:

```sh
docker-compose up -d
```

## Using Jupyter Notebook

Once the container is running, you can access Jupyter Notebook in your browser.

1. Open your browser and navigate to [http://localhost:8888](http://localhost:8888).
2. If prompted, enter the token provided in the terminal output.

### Creating and Running Notebooks

- To create a new notebook, click `New` -> `Python 3`.
- Use the `%matplotlib inline` magic command at the top of each cell where you intend to display plots.

Example setup cell in your Jupyter Notebook:

```python
# Setup cell
%matplotlib inline
import matplotlib.pyplot as plt
```

## Project Structure

The project directory contains the following files:

- `Dockerfile`: Defines the Docker image.
- `docker-compose.yml`: Defines the Docker services.
- `install_dependencies.sh`: Script to install required packages.
- `requirements.txt`: Python dependencies.
- `controller.py`: Main script to run network diagnostics.
- `model.py`: Contains core functions for network operations.
- `view.py`: Handles output formatting and plotting.

### Example `Dockerfile`

```Dockerfile
# Use the official Ubuntu image from the Docker Hub
FROM ubuntu:20.04

# Copy the install_dependencies.sh script into the container
COPY install_dependencies.sh /app/install_dependencies.sh

# Make the script executable
RUN chmod +x /app/install_dependencies.sh

# Run the script to install dependencies
RUN /app/install_dependencies.sh

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies listed in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the application
CMD ["python3", "controller.py"]
```

### Example `install_dependencies.sh`

```sh
#!/bin/bash

# Update package lists
apt-get update

# Install traceroute
apt-get install -y traceroute

# Install curl
apt-get install -y curl

# Install iputils-ping
apt-get install -y iputils-ping

# Install net-tools
apt-get install -y net-tools

# Install dnsutils
apt-get install -y dnsutils

# Install python3 and pip
apt-get install -y python3 python3-pip

# Install Python packages
pip3 install requests matplotlib ipwhois
```

## Functions Overview

### `model.py`

- `get_ip_address()`: Retrieves the local IP address.
- `check_https(url)`: Checks if a URL supports HTTPS.
- `traceroute(host)`: Performs a traceroute to the given host.
- `geolocate_ip(ip)`: Geolocates an IP address using IPWhois.

### `view.py`

- `print_ip_address(ip_address)`: Prints the local IP address.
- `print_https_check(url, is_secure)`: Prints HTTPS check results.
- `print_traceroute_output(traceroute_output)`: Prints traceroute results.
- `print_hop_info(hop, ip, latency, country, description)`: Prints hop information.
- `print_invalid_latency(line)`: Prints invalid latency lines.
- `plot_latency(hops, latencies)`: Plots traceroute latency.

### `controller.py`

This is the main script that orchestrates the execution of network diagnostics functions and displays the results.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
