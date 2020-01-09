FROM alpine:latest

WORKDIR /app

RUN apk -y update && apk -y upgrade

RUN apk install python3-pip -y

COPY . . 

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["/usr/bin/python3", "app.py"]