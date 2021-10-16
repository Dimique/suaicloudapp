#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install awscli -y
sudo apt install python3-pip -y
sudo apt install postgresql-client -y
sudo apt install libpq-dev -y

sudo mkdir /suai
cd /suai/
sudo git clone https://github.com/1k1ru/suaicloudapp.git
cd suaicloudapp/
sudo aws s3 sync s3://${bucket}/ .
pip3 install -r requirements.txt
python3 run.py
