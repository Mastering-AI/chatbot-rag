FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

COPY requirement.txt /app

RUN pip install --no-cache-dir -r requirement.txt

COPY . /app

EXPOSE 8000