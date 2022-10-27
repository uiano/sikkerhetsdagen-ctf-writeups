# Taskname
> Author: Mx. Task

## Challenge

## Solution

```python
import requests
import re
path = '5'
rex = re.compile(r'head to (.)')
while 1:
    resp = requests.get(f'http://127.0.0.1:5000/{path}', headers={'User-Agent': 'Googlebot'})
    if 'HEX-soup' in resp.text:
        print(bytes.fromhex(path))
        break
    path += rex.search(resp.text).group(1)
print(path)
```

<!-- Remove this comment once you are done with the writeup.
# What should be in the writeup.
-   The task analysis with clear explanations for what you found, don't assume something is "obvious" (because it might not be)
-   Explain the task itself, so that someone without in-depth knowledge of the challenge can also understand the idea
-   Include intermediate steps, eg. for crypto don't just write we arrive at equation XYZ, but actually provide the calculations
-   Include code snippets and examples/sanity checks for intermediate steps to "show" what is going on
-   The writeup should be in proper order, so it can be followed


# Writeup Examples

- https://github.com/tghack/tghack21/tree/main/Misc/Space_Calls/writeupLinks to an external site.
- https://github.com/tghack/tghack21/tree/main/Forensics/Internett_Of_Things_Ship/writeupLinks to an external site.
- https://github.com/tghack/tghack21/tree/main/Reversing/SpyingApache/writeup
--->
