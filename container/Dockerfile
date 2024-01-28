FROM python:3.10-slim

RUN apt-get update
RUN apt-get install --no-install-recommends --yes git libsodium23

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

WORKDIR /usr/local/var/
RUN git clone https://github.com/WebOfTrust/vLEI

WORKDIR /usr/local/var/vLEI
RUN pip install -r requirements.txt
