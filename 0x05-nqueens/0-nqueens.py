#!/usr/bin/python3
"""
N Queens Problem Solver
"""

import sys

def is_safe(board, row, col):
    """
    Check if a queen can be placed at the given
    cell without attacking others
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - row + i >= 0 and board[i][col - row + i] == 1:
            return False
        if col + row - i < len(board) and board[i][col + row - i] == 1:
            return False
    return True

def solve_nqueens(board, row):
    """
    Recursive function to solve N Queens problem
    """
    if row == len(board):
        print_solution(board)
        return
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0

def print_solution(board):
    """
    Print the solution in the required format
    """
    solution = []
    for row in board:
        for col in range(len(row)):
            if row[col] == 1:
                solution.append([col, row.index(1)])
    print(solution)

if __name__ == "__main__":
    """
    Handle command line arguments and solve the N Queens problem
    """
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
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_nqueens(board, 0)
