FROM alpine:latest

WORKDIR /app

RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base

COPY . . 

RUN pip install -r requirements.txt

EXPOSE 5003

ENTRYPOINT ["/usr/bin/python", "app.py"]