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


operators = ['+','-','*']

for l in "Kan du hjelpe meg løse disse 'få' tusen mattestykkene?:\n":
	sleep(0.1)
	print(l, end = '')


for i in range(1000):
	chosen_numbers = []
	chosen_operators = []
	numb_parts = (random.getrandbits(4) + 1)
	numb_operators = numb_parts - 1

	for i in range(numb_parts):
		chosen_numbers.append(random.getrandbits(10))

	for i in range(numb_operators):
		chosen_operators.append(random.choice(operators))

	final_string = f"{chosen_numbers[-1]}"

	for i in range(numb_operators):
		final_string += str(chosen_operators[i])
		final_string += str(chosen_numbers[i])

	solution = eval(final_string)
	print(f"{final_string} = ? ")

	try:
		input_from_client = int(input()) #Get string
	except:
		print("Error!")
		exit()
		break

	if int(input_from_client) != solution:
		for l in "Sorry, det er feil..\Korrekt: " + str(solution):
			sleep(0.1)
			print(l, end = '')
		exit()	

for l in f"For en fart!\n{FLAG}":
	sleep(0.1)
	print(l, end = '')		
