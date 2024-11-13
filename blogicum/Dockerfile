FROM python:3.12-slim

RUN apt-get update \
    && apt-get -y install libpq-dev gcc 

WORKDIR /blogicum

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .