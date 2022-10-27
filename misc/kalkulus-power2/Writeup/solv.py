from pwn import *

con = remote("ctf.uiactf.no", 5002)
con.recvuntil(b":\n")

for i in range(1000):
    equation_string = con.recvline().decode().strip()[:-3]
    solution = eval(equation_string)  # Hope no malicious content is returned
    con.sendline(str(solution).encode())

con.interactive()
