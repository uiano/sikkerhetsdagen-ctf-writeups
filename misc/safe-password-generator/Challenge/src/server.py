#!/usr/bin/python3
import random
import os

super_salt = str(random.getrandbits(50) + 1)

print("Velkommen til min superpassordmaskin9000v2!\n\
Gi meg en string som skal være med på å lage et nytt passord så skal jeg gi deg et skikkelig godt passord tilbake.\n\
(Begrenset til kun 2 ganger hver sesjon pga. sikkerhet..)")

for encryption_rounds in range(2):

	print(f"String:")
	input_from_client = input('> ')
	sha256_output = os.popen(f'echo "{input_from_client}" | sha256sum').read()
	
	i = 0
	while len(super_salt) < len(sha256_output):
		super_salt += super_salt[i]
		i += 1

	new = [(hex(ord(a) ^ ord(b)))[2:] for a,b in zip(super_salt, sha256_output)]


	print(f"Her er ditt gode password:\n> {''.join(new)}")