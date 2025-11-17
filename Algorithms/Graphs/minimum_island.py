# minimum island

# https://structy.net/problems/minimum-island

grid_1 = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]
grid_2 = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]
grid_3 = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]
grid_4 = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

def minimum_island(grid: list[list[str]]) -> int:
    visited = {}
    min_count = len(grid) * len(grid[0])

    for r in range(len(grid)):
        for c in range(len(grid[0])):
           count = _dfr_helper(grid, r, c, visited)
           # if statement neccessary to prevent always returning zero.
           min_count =  min(min_count, count) if count else min_count
    return min_count

def _dfr_helper(grid: list[list[str]], r: int, c: int, visited: dict[str, int]):
    is_rows_inbound = 0 <= r < len(grid)
    is_cols_inbound = 0 <= c < len(grid[0])
    if not is_rows_inbound or not is_cols_inbound:
        return 0

    if grid[r][c] == 'W':
        return 0
    
    node = f"{r},{c}"
    if node in visited:
        return 0
    

    visited[node] = 1

    count = 1

    count += _dfr_helper(grid, r - 1, c, visited)
    count += _dfr_helper(grid, r + 1, c, visited)
    count += _dfr_helper(grid, r, c - 1, visited)
    count += _dfr_helper(grid, r, c + 1, visited)

    return count

# r = number of rows
# c = number of columns
# O(r * c) Time complexity
# O(r * c) Space complexity

print(minimum_island(grid_1)) # -> 2
print(minimum_island(grid_2))  # -> 1
print(minimum_island(grid_3))  # -> 9
print(minimum_island(grid_4))  # -> 1
