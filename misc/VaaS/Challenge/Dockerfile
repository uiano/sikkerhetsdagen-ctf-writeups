FROM python:3.10.7

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf
WORKDIR /home/ctf
COPY ./src/. .

RUN apt-get update && apt-get install -y socat vim && rm -rf /var/lib/apt/lists/*

USER ctf

CMD socat \
    TCP-LISTEN:1337,nodelay,reuseaddr,fork \
    EXEC:"stdbuf -i0 -o0 -e0 vim"