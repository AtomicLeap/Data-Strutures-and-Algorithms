# island count

# https://structy.net/problems/island-count

# NOTE: Grid Graph
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
  ['W', 'W'],
  ['W', 'W'],
]

def island_count(grid: list[list[str]]) -> int:
    visited = {}
    count = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
           if _dfr_helper(grid, r, c, visited):
               count += 1
    return count

def _dfr_helper(grid: list[list[str]], r: int, c: int, visited: dict[str, int]):
    is_rows_inbound = 0 <= r < len(grid)
    is_cols_inbound = 0 <= c < len(grid[0])
    if not is_rows_inbound or not is_cols_inbound:
        return False
    
    if grid[r][c] == 'W':
        return False
    
    node = f"{r},{c}"
    if node in visited:
        return False
    
    visited[node] = 1
    
    _dfr_helper(grid, r - 1, c, visited)
    _dfr_helper(grid, r + 1, c, visited)
    _dfr_helper(grid, r, c - 1, visited)
    _dfr_helper(grid, r, c + 1, visited)

    return True

# r = number of rows
# c = number of columns
# O(r * c) Time complexity
# O(r * c) Space complexity

print(island_count(grid_1)) # -> 3
print(island_count(grid_2)) # -> 4
print(island_count(grid_3)) # -> 1
print(island_count(grid_4)) # -> 0