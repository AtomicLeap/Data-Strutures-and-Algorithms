# sudoku solver


# STEPS
# 1. Find an empty spot.
#       a. if found, return empty spot.
#       b. if no empty spot found, return True (Fully solved)
# 2. Try a guess, 
# 3. Check validity of guess;
#       a. if guess is valid, replace empty spot with guess; And continue recursively.
#       b. if guess not valid, we set empty spot with zero.

from pprint import pprint

def find_empty_spot(puzzle: list[list[int]], m, n) -> tuple[int, int] | tuple[None, None]:
    for i in range(m):
        for j in range(n):
            if not puzzle[i][j]:
                return (i, j)
    return (None, None)

def is_guess_valid(puzzle: list[list[int]], guess: int, row: int, col: int) -> bool:
    row_values = puzzle[row]
    col_values = [row_item[col] for row_item in puzzle]

    if guess in row_values or guess in col_values:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if guess == puzzle[i][j]:
                return False
    return True

def sudoku_solver(puzzle: list[list[int]]) -> bool:
    m = len(puzzle)
    n = len(puzzle[0])

    (row, col) = find_empty_spot(puzzle, m, n)

    if row == None or col == None:
        print('solved sudoku: \n')
        pprint(puzzle)
        return True
    
    for guess in range(1, 10):
        if is_guess_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if sudoku_solver(puzzle):
                return True
        puzzle[row][col] = 0
    return False



puzzle = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]

print(sudoku_solver(puzzle))