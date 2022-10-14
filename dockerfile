FROM debian:11

WORKDIR /nucliadb

COPY . .

RUN apt-get update && apt-get install python3 python3-pip -y

RUN chmod +x ./install.sh

EXPOSE 8080 8080

ENTRYPOINT ["./install.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
