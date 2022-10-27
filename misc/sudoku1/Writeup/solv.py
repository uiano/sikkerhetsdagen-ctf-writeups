from pwn import *


con = remote("ctf.uiactf.no", 5005)


def get_solution_string(board):
    # Get the solution string
    solv_string = ""
    for outer in board:
        for inner in outer:
            solv_string += str(inner)

    return solv_string


def shortSudokuSolve(board):
    size = len(board)
    block = int(size**0.5)
    board = [n for row in board for n in row]
    span = {
        (n, p): {
            (g, n)
            for g in (n > 0)
            * [
                p // size,
                size + p % size,
                2 * size + p % size // block + p // size // block * block,
            ]
        }
        for p in range(size * size)
        for n in range(size + 1)
    }
    empties = [i for i, n in enumerate(board) if n == 0]
    used = set().union(*(span[n, p] for p, n in enumerate(board) if n))
    empty = 0
    while empty >= 0 and empty < len(empties):
        pos = empties[empty]
        used -= span[board[pos], pos]
        board[pos] = next(
            (n for n in range(board[pos] + 1, size + 1) if not span[n, pos] & used), 0
        )
        used |= span[board[pos], pos]
        empty += 1 if board[pos] else -1
        if empty == len(empties):
            solution = [board[r : r + size] for r in range(0, size * size, size)]
            return solution


for i in range(20):
    con.recvuntil(b":\n")

    board = []
    for i in range(4):
        t_line = con.recvline().decode().strip().strip("][").split(",")
        line = [int(a) for a in t_line]
        board.append(line)

    solved_board = shortSudokuSolve(board)
    solution_string = get_solution_string(solved_board)
    print(solution_string)
    con.sendline(solution_string.encode())

print(con.interactive())
