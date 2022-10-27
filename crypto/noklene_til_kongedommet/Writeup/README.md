# Taskname
> Author: Mx. Task

## Challenge

## Solution
Her får vi ciphertext som hex, og en zip fil med masse RSA sertifikater. Enn vet at modulo N er beregnet med 2 primtall p og q som er ganget sammen, men det er mulig at to (eller flere sertifikater) deler samme primtall. Da vil Greatest Common Divisor (gcd) av de 2 moduloene ikke være 1. Mao. vi kan bruteforce par av sertifikater til vi finner en delt faktor, for så å teste om vi får dekryptert meldingen.

```python
from Cryptodome.Util.number import inverse, long_to_bytes, bytes_to_long
from Cryptodome.PublicKey import RSA
import zipfile
from itertools import combinations
from math import gcd

# Last inn alle RSA nøklene
zip_file = zipfile.ZipFile('keys.zip','r')
keys = []
for name in zip_file.namelist():
    data = zip_file.read(name)
    key = RSA.import_key(data)
    keys.append(key)

e = 0x10001
ct = bytes_to_long(bytes.fromhex(open('ciphertext.hex','r').read()))
# Loop over alle kombinasjoner av 2 nøkler
for k1, k2 in combinations(keys, 2):
    # Sjekk om de deler faktor
    if gcd(k1.n, k2.n) == 1: continue
    print("Found match")
    # Finner delt faktor, så kalkulerer den andre og dekrypterer meldingen
    shared_p = gcd(k1.n, k2.n)
    q1 = k1.n // shared_p
    q2 = k2.n // shared_p

    d1 = inverse(e, (shared_p-1)*(q1-1))
    d2 = inverse(e, (shared_p-1)*(q2-1))

    print(long_to_bytes(pow(ct, d1, k1.n)))
    print(long_to_bytes(pow(ct, d2, k2.n)))
    break
```
