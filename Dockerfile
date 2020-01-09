FROM alpine:latest

WORKDIR /app

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

COPY . . 

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/bin/python3", "app.py"]