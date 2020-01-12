#! bin/bash

sudo apt-get -y update 
sudo apt-get install git -y
sleep 5
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo curl https://get.docker.com | sudo bash
sleep 10
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $(whoami)
sudo systemctl restart docker
source ~/.bashrc
git clone https://github.com/TomLLew/DwarvenGenerator.git
cd DwarvenGenerator
git checkout compose
docker-compose up -d --build


echo "restart your terminal!"