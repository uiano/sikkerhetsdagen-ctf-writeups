#!/usr/bin/python3
import sys
import socket
from threading import Thread
import traceback
import json
from time import sleep
import random


FLAG = ""
with open('flag.txt','r') as fh:
	FLAG = fh.readline()

for l in "Kan du hjelpe meg løse disse 'få' tusen mattestykkene?:\n":
	sleep(0.1)
	print(l, end = '')

for i in range(1000):
	numb1 = random.getrandbits(10)
	numb2 = random.getrandbits(10)
	solution = numb1+numb2
	print(f"{numb1} + {numb2} = ? ")

	try:
		input_from_client = int(input()) #Get string
	except:
		print("Error!")
		exit()
		break

	if int(input_from_client) != solution:
		#Cleanup
		for l in "Sorry, det er feil..\Korrekt: " + str(solution):
			sleep(0.1)
			print(l, end = '')
		exit()  # close connection	

for l in f"For en fart!\n{FLAG}":
	sleep(0.1)
	print(l, end = '')		
