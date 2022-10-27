#!/usr/bin/python3
import os

print("Velkommen til min superpassordmaskin9000v1!\n\
Gi meg en string som skal være med på å lage et nytt passord så skal jeg gi deg et skikkelig godt passord tilbake.")
print(f"String:")

input_from_client = input('> ')
sha256_output = os.popen(f'echo "{input_from_client}" | sha256sum').read()

print(f"Her er ditt gode password:\n> {''.join(sha256_output)}")