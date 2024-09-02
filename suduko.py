import pyautogui as pg
import numpy as np
import time

# Class-based Sudoku Solver
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        self.solve(board)

    def solve(self, board: list[list[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in '123456789':
                        if self.isValid(i, j, c, board):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def isValid(self, row: int, col: int, c: str, board: list[list[str]]) -> bool:
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == c:
                return False
        return True

# Input Handling
grid = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

time.sleep(5)

# Convert grid to a format compatible with the Solution class
board = [['.' if num == 0 else str(num) for num in row] for row in grid]

# Solve the Sudoku
solver = Solution()
solver.solveSudoku(board)

# Convert the board back to the original format
grid = [[int(num) if num != '.' else 0 for num in row] for row in board]

# Function to print the solved Sudoku using PyAutoGUI
def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            for _ in range(8):
                pg.hotkey('left')

# Print the solved Sudoku
Print(grid)
input("More?")
