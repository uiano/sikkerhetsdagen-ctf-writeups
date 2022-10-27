FROM python:3.10.7

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf
WORKDIR /home/ctf
COPY ./src/. .

RUN chmod a+x /home/ctf/server.py
RUN chmod a+x /home/ctf/sudo_generator.py

RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/*

USER ctf

CMD socat \
    TCP-LISTEN:1337,reuseaddr,fork \
    EXEC:"python -u /home/ctf/server.py"