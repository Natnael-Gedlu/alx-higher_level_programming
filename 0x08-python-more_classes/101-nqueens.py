#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.
"""

import sys


def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        for r in range(row):
            if board[r] == col or \
                    board[r] - r == col - row or \
                    board[r] + r == col + row:
                return False
        return True

    def backtrack(row, board):
        if row == N:
            return [board[:]]

        solutions = []
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solutions.extend(backtrack(row + 1, board))
        return solutions

    solutions = backtrack(0, [-1] * N)

    for solution in solutions:
        for col in solution:
            row_str = "." * col + "Q" + "." * (N - col - 1)
            print(row_str)
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
