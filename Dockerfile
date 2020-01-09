FROM alpine:latest

WORKDIR /app

RUN apk update && apk upgrade

RUN apk add python3-pip 

COPY . . 

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/bin/python3", "app.py"]