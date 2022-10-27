import math

if __name__ == '__main__':
    print("Welcome to the calculator!")
    while 1:
        to_calculate = input('> ')
        print(eval(to_calculate, {'math': math, '__builtins__': {}}, {}))
