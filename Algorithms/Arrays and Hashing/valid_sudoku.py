# Leetcode 36. Valid Sudoku

# https://leetcode.com/problems/valid-sudoku/description/


# Iterative solution -> (Validate filled cells (positions))

def valid_sudoku(board: list[list[str]]) -> bool:
    m, n = len(board), len(board[0])

    def _is_valid_cell(cell_value: int, row: int, col: int):
        row_values = board[row]
        col_values = [row_vals[col] for row_vals in board]

        # Check Rows and Columns are valid
        if cell_value in row_values or cell_value in col_values:
            return False
        
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3

        # Check if 3 X 3 box is valid
        for r in range(row_start, row_start + 3):
            for c in range(col_start, col_start + 3):
                if board[r][c] == cell_value:
                    return False
        return True

    for row in range(m):
        for col in range(n):
            if board[row][col] == ".":
                continue
            
            cell_value = board[row][col]
            board[row][col] = "#" # Mark position as visited

            if not _is_valid_cell(cell_value, row, col):
                board[row][col] = cell_value # Backtrack
                return False
            board[row][col] = cell_value # Backtrack
    return True

# O(81) ≈ O(1) (or O(n²) if generalized to n×n) - Time complexity
# O(1) - Space complexity


board_1 =   [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

board_2 =   [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
# Output: false

print(valid_sudoku(board_1)) # True
print(valid_sudoku(board_2)) # False
