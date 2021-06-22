#!/bin/bash
VIRTUALENV=/home/ubuntu/venv

pushd $(dirname "$0")
source $VIRTUALENV/bin/activate
cd /home/ubuntu
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port 8080 >/dev/null 2>&1 &
