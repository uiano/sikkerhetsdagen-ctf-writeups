from pwn import *


con = remote("ctf.uiactf.no", 5006)

# This function will decide the least possible value for an empty space, r stands for row index, c for column index
def decide(r, c):
    # As you can see, a and b will decide the native 3/3 square for a particular index
    a, b = r // 3 * 3, c // 3 * 3
    # If a number has index (5, 6) you will get a=3, b=6 this means the 3/3 square extends
    # over row 3,4,5 and column 6,7,8
    # After back tracking let's say our value is 5, this loop will check where 6, 7, 8, 9 are fit for being used.
    # If the spot is zero, it just starts from 1 and goes up to 9 until a suitable value if found
    for i in range(board[r][c] + 1, 10):
        for j in range(9):
            # board[r][j] checks whether the number i is there in the row r
            # board[j][c] checks whether the number i is there in the column c
            # board[a+j//3][b+j % 3] try to dry run the values j//3 and j%3 you'll understand.
            # j//3 will give 0, 0, 0, 1, 1, 1, 2, 2, 2 over the 9 iterations.
            # j%3  will give 0, 1, 2, 0, 1, 2, 0, 1, 2 over the 9 iterations.
            # Let's say you have a=3 and b=6
            # a+j//3 will extend over 3, 3, 3, 4, 4, 4, 5, 5, 5
            # b+j%3 will give        :6, 7, 8, 6, 7, 8, 6, 7, 8
            # Thus we cover the entire 3/3 square, also the row and the column.
            if (
                board[r][j] == i
                or board[j][c] == i
                or board[a + j // 3][b + j % 3] == i
            ):
                # obviously if any of these is true, the number is not fit
                break
        else:
            # if a number is found to be fit it is returned immediately
            return i
    # if no solution can be found, zero is returned. This means there has been some mistake with the previous solution, we'll back trace in the solve function and fix thaht.
    return 0


def solve():
    # mutable collects the indices of all the empty spots.
    mutable = [
        (i, j)
        for i, row in enumerate(board)
        for j, element in enumerate(row)
        if element == 0
    ]
    i = 0
    while i < len(mutable):
        r, c = mutable[i]
        # we send the row and column no. of the empty spot to decide function
        board[r][c] = decide(r, c)
        # If a solution has been found, we just go on, if a zero is returned that means something's been wrong, we backtrace, reduce the value of i by i
        if board[r][c] == 0:
            i -= 1
            continue
        i += 1


def print_board():
    for i in range(len(board)):
        if i % 3 == 0:
            print("-" * 23)
        for j in range(len(board[i])):
            if j != 0 and j % 3 == 0:
                print(" | ", end="")
            print(board[i][j], end=" ")
        print()
    print("-" * 23)


def get_solution_string(board):
    # Get the solution string
    solv_string = ""
    for outer in board:
        for inner in outer:
            solv_string += str(inner)

    return solv_string


from timeit import timeit


for i in range(50):
    con.recvuntil(b":\n")

    board = []
    for i in range(9):
        t_line = con.recvline().decode().strip().strip("][").split(",")
        line = [int(a) for a in t_line]
        board.append(line)

    time = timeit(solve, number=1)
    solv = get_solution_string(board)
    print(get_solution_string(board))
    print(f"Finished in {time}s")
    con.sendline(solv.encode())

print(con.interactive())
