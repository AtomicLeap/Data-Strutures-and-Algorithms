# Leetcode 695. Max Area of Island

# https://leetcode.com/problems/max-area-of-island/description/

# Tags -> Depth-First Search, Breadth-First Search, Union-Find, Matrix

def max_area_of_island(grid: list[list[int]]) -> int:
    r = len(grid)
    c = len(grid[0])
    max_count = 0

    def dfs(row: int, col: int, visited: set):
        row_in_bounds = 0 <= row < r
        col_in_bounds = 0 <= col < c

        if not row_in_bounds or not col_in_bounds:
            return 0
        
        if grid[row][col] == '0':
            return 0
        
        cell = f"{row},{col}"

        if cell in visited:
            return 0
        
        visited.add(cell)
        count = 1

        count += dfs(row - 1, col, visited)
        count += dfs(row + 1, col, visited)
        count += dfs(row, col - 1, visited)
        count += dfs(row, col + 1, visited)

        return count
    for row in range(r):
        for col in range(c):
            count = dfs(row, col, set())
            max_count = max(count, max_count)
    return max_count

# Let r, c = len(grid), len(grid[0])
# O(r * c) - Time complexity
# O(r* c) - Space complexity

print(max_area_of_island([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                          [0,0,0,0,0,0,0,1,1,1,0,0,0],
                          [0,1,1,0,1,0,0,0,0,0,0,0,0],
                          [0,1,0,0,1,1,0,0,1,0,1,0,0],
                          [0,1,0,0,1,1,0,0,1,1,1,0,0],
                          [0,0,0,0,0,0,0,0,0,0,1,0,0],
                          [0,0,0,0,0,0,0,1,1,1,0,0,0],
                          [0,0,0,0,0,0,0,1,1,0,0,0,0]])) # 6
print(max_area_of_island([[0,0,0,0,0,0,0,0]])) # 0