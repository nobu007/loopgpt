# Use an official Python base image from the Docker Hub
FROM ubuntu:latest AS loopgpt-base

RUN apt-get update && apt-get install -y python3 python3-pip

# aptの対話を無効にしてデフォルトの地理的なエリアを設定
ENV DEBIAN_FRONTEND=noninteractive
RUN echo 'Etc/UTC' > /etc/timezone 

# Install browsers
RUN apt update && apt install -y \
    firefox \
    ca-certificates

# Install utilities
RUN apt install -y curl jq wget git gcc g++ libc-dev bash

# Install curl library
RUN apt install -y libcurl4-openssl-dev

# Set environment variables
ENV PIP_NO_CACHE_DIR=yes \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt setup.py ./
COPY loopgpt ./loopgpt
COPY examples ./examples
RUN chmod -R 755 .

RUN pip3 install -e .
RUN pip3 install comet_llm google-generativeai momento langchain_google_genai langchain python-dotenv sentence-transformers

ENV DISPLAY=:99 \
    PATH=/root/.local/bin:$PATH

COPY yka_langchain.py ./loopgpt/models/yka_langchain.py

# ENTRYPOINT ["loopgpt", "run"]
ENTRYPOINT ["bash"]

