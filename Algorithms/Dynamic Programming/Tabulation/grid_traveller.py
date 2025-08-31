# Grid Traveller
# How many ways can a traveller travel to the bottom right end in an m x n grid

"""
Say that you are a traveller on a 2D grid. You begin in the top-left corner 
and your goal is to travel to the bottom-right corner. You may only move
down or right. In how many ways can you travel to the goal on a grid with
dimensions m * n?

Write a function 'grid_traveller(m, n)' that calculates this.
"""

# Tabulation solution
def grid_traveller(m: int, n: int) -> int:
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if i + 1 < m + 1:
                table[i + 1][j] += table[i][j]
            if j + 1 < n + 1:
                table[i][j + 1] += table[i][j]
    return table[m][n]


# O(m * n) Time complexity
# O(m * n) Space complexity

print(grid_traveller(1, 1)) # 1
print(grid_traveller(3, 1)) # 1
print(grid_traveller(2, 3)) # 3
print(grid_traveller(3, 2)) # 3
print(grid_traveller(3, 3)) # 6
print(grid_traveller(3, 3)) # 6
print(grid_traveller(20, 20)) # 35345263800
