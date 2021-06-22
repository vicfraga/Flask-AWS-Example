#!/bin/bash
cd /home/ubuntu
sudo apt-get update
sudo apt-get install -y virtualenv python2.7 python-pip
mkdir venv
virtualenv venv
source venv/bin/activate
sudo locale-gen pt_BR.UTF-8
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
pip install -r requirements.txt
