# Taskname
> Author: Mx. Task

## Challenge

## Solution

Teksten ser ut til å beholde flaggformatet. Oppgavenavnet hinter vagt til en form for ROT, med `Rot`en.
Dessverre fungerer ikke vanlig ROT13, enn kan også se at `æøå` er inkludert.
Heldigvis har vi kjent plaintext, `UIACTF{` som vi kan benytte oss av!
Ved litt testing vil enn se at differansen er konstant + en "counter" verdi, vi kan da bruteforce hele systemet til vi finner flagget

```python
from string import ascii_lowercase as al

al = al + 'æøå'
au = al.upper()

def decrypt(s, k):
    pt = ''
    for i, c in enumerate(s):
        if c in al:
            pt += al[(al.index(c) - k - i) % len(al)]
        elif c in au:
            pt += au[(au.index(c) - k - i) % len(au)]
        else:
            pt += c
    return pt

for k in range(1, 29):
    print(decrypt(ct, k))
```

