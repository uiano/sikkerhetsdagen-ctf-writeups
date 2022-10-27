#!/usr/bin/python3
import sys
import socket
from threading import Thread
import traceback
import json
from time import sleep
import random
from itertools import islice

from sudo_generator import SudokuGenerator

target_solves = 50
flag = ""
with open('flag.txt','r') as fh:
	flag = fh.readline()

def get_solution_string(board):
    # Get the solution string
    solv_string = ""
    for outer in board:
        for inner in outer:
            solv_string += str(inner)

    return solv_string

solves = 0
for i in range(target_solves):
	print("Løs dette:")

	generator = SudokuGenerator()
	solved_board = generator.grid
	solution_string = get_solution_string(solved_board)
	generator.remove_numbers_from_grid()	
	unsolved_board = generator.grid

	#print(solution_string)
	# Send board
	for line in unsolved_board:
		line = [str(a) for a in line]
		print(f"[{','.join(line)}]")	

	attempt = input() #Get string

	if attempt == solution_string:
		print("Korrekt!")
		solves += 1
	else:
		print(f"Error!\nLøsning:\n{solution_string}")
		exit()


if solves == target_solves:
	print(f"Flag: {flag}")
