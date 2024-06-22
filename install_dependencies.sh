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
