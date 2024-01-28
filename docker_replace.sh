#!/bin/bash

# get current directory
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo "CURRENT_DIR=$CURRENT_DIR"

# rm ~/.config/ailice/config.json
cd $CURRENT_DIR
# copy all files to docker
docker cp .env loopgpt:/app/.env
docker cp examples loopgpt:/app/
docker cp loopgpt loopgpt:/app/
docker cp yka_langchain.py loopgpt:/app/yka_langchain.py

# restart docker
echo "Restarting docker..."
# docker restart loopgpt
echo "Restarting docker...done"