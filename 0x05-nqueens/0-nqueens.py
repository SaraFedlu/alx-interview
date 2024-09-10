#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    """Check if placing a queen at (row, col) is valid."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions."""
    def backtrack(row):
        if row == N:
            # Found a solution; convert it into the required format
            solution = [[i, board[i]] for i in range(N)]
            print(solution)
            return

        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                # No need to "undo" since each recursion starts fresh

    board = [-1] * N  # represent the column index of queen in row i
    backtrack(0)


if __name__ == "__main__":
    # Argument validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
