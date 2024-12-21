FROM python:3.12.6-slim AS builder

# Install compilation dependencies for Ubuntu including ca-certificates, libffi, and libsodium
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libsodium-dev \
    libssl-dev \
    python3-dev \
    python3-venv \
    python3-pip \
    curl

SHELL ["/bin/bash", "-c"]

# Setup Rust for blake3 dependency build
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

WORKDIR /vLEI

RUN python -m venv venv
ENV PATH=/vLEI/venv/bin:${PATH}
RUN pip install --upgrade pip

COPY requirements.txt setup.py /vLEI/
RUN mkdir /vLEI/src

# Build vLEI-server
RUN . "$HOME/.cargo/env" && \
    pip install -r requirements.txt

# Create smaller runner image by copying over built binary
FROM python:3.12.6-slim AS runner

RUN apt-get update
RUN apt-get install -y libsodium23 curl

# Prevents Python from buffering stdout and stderr, logs to stdout immediately
ENV PYTHONUNBUFFERED=1
# Set default encoding to UTF-8
ENV PYTHONIOENCODING=UTF-8

WORKDIR /vLEI

COPY --from=builder /vLEI /vLEI
COPY src/ src/
COPY ./schema/acdc /vLEI/schema
COPY ./samples/acdc /vLEI/credentials
COPY ./samples/oobis /vLEI/oobis

ENV PATH=/vLEI/venv/bin:${PATH}

CMD ["vLEI-server", "-s", "/vLEI/schema", "-c", "/vLEI/credentials", "-o", "/vLEI/oobis"]
