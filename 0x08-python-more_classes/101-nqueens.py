#!/usr/bin/python3
"""Solves the N Queens problem.

Usage: nqueens N

This program finds and prints all possible solutions to the N Queens problem,
where N is the number of non-attacking queens to be placed on an N×N chessboard.

Args:
    N (int): The size of the chessboard and the number of queens.

If the user provides the wrong number of arguments or N is not a valid integer,
the program prints an error message and exits with status 1.

N must be an integer greater than or equal to 4. If N is smaller than 4,
the program prints an error message and exits with status 1.

"""

import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen in the given row and column."""
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':
            return False

    return True


def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions."""
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        if row == N:
            solutions.append(["".join(row) for row in board])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
