#!/bin/bash

# get current directory
CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
echo "CURRENT_DIR=$CURRENT_DIR"

# copy .env and yka_langchain.py to docker build context
cp -p "${CURRENT_DIR}/../.env" "${CURRENT_DIR}/.env"
cp -p "${CURRENT_DIR}/../../common/yka_langchain.py" "${CURRENT_DIR}/yka_langchain.py"
echo $MOMENTO_AUTH_TOKEN

docker build --progress plain -t loopgpt:local-dev .
