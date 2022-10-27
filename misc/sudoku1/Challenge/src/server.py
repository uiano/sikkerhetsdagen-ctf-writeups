#!/usr/bin/python3
import sys
import socket
from threading import Thread
import traceback
import json
from time import sleep
import random
from itertools import islice

target_solves = 20
base  = 2
side  = base*base
flag = ""
with open('flag.txt','r') as fh:
	flag = fh.readline()

def get_solution_string(provided_board):
    # Get the solution string
    solv_string = ""
    for outer in provided_board:
        for inner in outer:
            solv_string += str(inner)

    return solv_string

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)

def shuffle(s): return random.sample(s,len(s)) 

def generate_board():
	rBase = range(base) 
	rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
	cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
	nums  = shuffle(range(1,base*base+1))

	# produce board using randomized baseline pattern
	new_board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
	return new_board

def remove_numbers(inp_board):
	squares = side*side
	empties = squares * 1//2
	for p in random.sample(range(squares),empties):
		inp_board[p//side][p%side] = 0
	return inp_board


def shortSudokuSolve(board):
    size    = len(board)
    block   = int(size**0.5)
    board   = [n for row in board for n in row ]      
    span    = { (n,p): { (g,n)  for g in (n>0)*[p//size, size+p%size, 2*size+p%size//block+p//size//block*block] }
                for p in range(size*size) for n in range(size+1) }
    empties = [i for i,n in enumerate(board) if n==0 ]
    used    = set().union(*(span[n,p] for p,n in enumerate(board) if n))
    empty   = 0
    while empty>=0 and empty<len(empties):
        pos        = empties[empty]
        used      -= span[board[pos],pos]
        board[pos] = next((n for n in range(board[pos]+1,size+1) if not span[n,pos]&used),0)
        used      |= span[board[pos],pos]
        empty     += 1 if board[pos] else -1
        if empty == len(empties):
            solution = [board[r:r+size] for r in range(0,size*size,size)]
            yield solution
            empty -= 1

solves = 0

for i in range(target_solves):
	print("Løs dette:")

	only_one_solv = False
	while True:
		solved_board = generate_board()
		unsolved_board = remove_numbers(solved_board)
		# Try to solve 10 times, if not successful just create a new board
		for i in range(10):
			solved  = [*islice(shortSudokuSolve(unsolved_board),2)]
			if len(solved)==1:
				only_one_solv = True
				break
			diffPos = [(r,c) for r in range(side) for c in range(side)
					if solved[0][r][c] != solved[1][r][c] ] 
			r,c = random.choice(diffPos)
			unsolved_board[r][c] = solved_board[r][c]
		if only_one_solv:
			break

	solution_string = get_solution_string(solved[0])
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