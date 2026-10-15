FROM gleif/keri:1.2.16@sha256:00cb71627b2cb5999d09b2934bd28b3fc762149ae9678fab38698fba7418cd06

ENV PYTHONUNBUFFERED=1 PYTHONIOENCODING=UTF-8
WORKDIR /vLEI
COPY setup.py README.md LICENSE /vLEI/
COPY src/ /vLEI/src/
RUN python -m pip install --no-cache-dir . && python -m pip check
COPY schema/acdc/ /vLEI/schema/
COPY samples/acdc/ /vLEI/credentials/
COPY samples/oobis/ /vLEI/oobis/

CMD ["vLEI-server", "-s", "/vLEI/schema", "-c", "/vLEI/credentials", "-o", "/vLEI/oobis"]
