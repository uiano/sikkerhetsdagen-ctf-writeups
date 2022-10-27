import requests
import re
path = '5'
rex = re.compile(r'head to (.)')
while 1:
    resp = requests.get(f'http://ctf.uiactf.no:3002/{path}', headers={'User-Agent': 'Googlebot'})
    if 'HEX-soup' in resp.text:
        print(bytes.fromhex(path))
        break
    path += rex.search(resp.text).group(1)
print(path)