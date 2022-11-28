#!/bin/bash
sudo apt update
sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y
docker --version

# Install docker-compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.13.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

# Install repo
git clone https://github.com/nanterre-people/info-night-2022.git
cd info-night-2022

# Launch project with docker-compose
# docker-compose up -d