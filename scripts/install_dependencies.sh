#!/bin/bash
cd /home/ubuntu
sudo apt-get update
sudo apt-get install -y python2.7 python-pip
pip install -r requirements.txt
