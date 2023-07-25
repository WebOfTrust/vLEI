FROM gleif/keri:1.0.0

ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8

WORKDIR /app
COPY ./ ./
RUN pip install -r requirements.txt

EXPOSE 7723

ENTRYPOINT [ "vLEI-server", "-s", "./schema/acdc", "-c" , "./samples/acdc/", "-o", "./samples/oobis/" ]