FROM alpine:latest

WORKDIR /app

RUN apt-get -y update && apt-get -y upgrade

RUN apt-get install python3-pip -y

COPY . . 

RUN pip3 install -r requirements.txt

EXPOSE 5001

ENTRYPOINT ["/usr/bin/python3", "app.py"]