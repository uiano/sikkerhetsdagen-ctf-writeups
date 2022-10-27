# Taskname
> Author: Mx. Task

## Challenge

## Solution

Kan virke som monoalfabestisk cipher på repeterende karakterer.
En fin -> a fine -> affine cipher
Bruk at vi vet starten på flagget som "known plaintext", og bruteforce `a` og `b`
```python
from Cryptodome.Util.number import inverse
def decrypt(s, a, b):
    pt = ''
    ai = inverse(a, len(al))
    for c in s:
        if c in al:
            pt += al[(ai*(al.index(c) - b)) % len(al)]
        elif c in au:
            pt += au[(ai*(au.index(c) - b)) % len(au)]
        else:
            pt += c
    return pt
ct = ''
for a in range(0, 10):
    for b in range(0, 10):
        pt = decrypt(ct, a, b)
        if pt.startswith('UIACTF'):
            print(pt)
```

