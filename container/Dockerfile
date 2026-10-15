FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1

RUN apt-get update && apt-get install -y --no-install-recommends libsodium23 curl \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8
WORKDIR /vLEI
COPY setup.py README.md LICENSE /vLEI/
COPY src/ /vLEI/src/
RUN python -m pip install --no-cache-dir . && python -m pip check
COPY schema/acdc/ /vLEI/schema/
COPY samples/acdc/ /vLEI/credentials/
COPY samples/oobis/ /vLEI/oobis/

CMD ["vLEI-server", "-s", "/vLEI/schema", "-c", "/vLEI/credentials", "-o", "/vLEI/oobis"]
