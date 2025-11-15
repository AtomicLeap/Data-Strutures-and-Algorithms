# Leetcode 200. Number of Islands

# https://leetcode.com/problems/number-of-islands/description/

def num_of_islands(grid: list[list[str]]) -> int:
    visited = set()
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if _explore_dfr_helper(grid, row, col, visited) == True:
                count += 1

    return count

def _explore_dfr_helper(grid: list[list[str]], row: int, col: int, visited: set[str]):
    is_row_inbound = 0 <= row < len(grid)
    is_col_inbound = 0 <= col < len(grid[0])
    # checks 1
    if not is_row_inbound or not is_col_inbound:
        return False
    
    # checks 2
    if grid[row][col] == "0":
        return False
    
    # checks 3
    pos = f"{row},{col}"
    if pos in visited:
        return False

    # Add to visited
    visited.add(pos)

    _explore_dfr_helper(grid, row - 1, col, visited)
    _explore_dfr_helper(grid, row + 1, col, visited)
    _explore_dfr_helper(grid, row, col - 1, visited)
    _explore_dfr_helper(grid, row, col + 1, visited)

    return True

# r = number of rows
# c = number of columns
# O(r * c) Time complexity
# O(r * c) Space complexity

grid_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# Output: 1

grid_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# Output: 3

print(num_of_islands(grid_1)) # 1
print(num_of_islands(grid_2)) # 3