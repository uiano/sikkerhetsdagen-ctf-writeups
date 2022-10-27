#!/usr/bin/env python3
import math

if __name__ == '__main__':
    print("Velkommen til min enkle kalkulator!\nSkriv inn det du vil beregne etter '>' og du får et svar!")
    while 1:
        to_calculate = input('> ')
        print(eval(to_calculate))
