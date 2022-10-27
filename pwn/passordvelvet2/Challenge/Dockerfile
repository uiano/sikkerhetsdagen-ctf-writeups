FROM ubuntu:20.04

RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY ./src/. .
COPY ./conf/ynetd .

RUN chown -R root:root /home/ctf
RUN chmod +x ynetd
RUN chmod +x passordvelvet2

USER ctf
EXPOSE 1337
CMD ./ynetd -p 1337 ./passordvelvet2