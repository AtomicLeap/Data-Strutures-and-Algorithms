# Grid Traveller
# How many ways can a traveller travel to the bottom right end in an m x n grid

# Brute force solution
def grid_traveller(n: int, m: int) -> int:
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
# O(2^(m + n)) Time complexity = > 2 recursive calls
# O(m + n) Space complexity => max stack depth of n

# Optimized solution
def grid_travellero(m: int, n: int, memo: dict = {}) -> int:
    key = f"{m},{n}"
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_travellero(m - 1, n, memo) + grid_travellero(m, n - 1, memo)
    return memo[key]
# O(m * n) Time complexity = > memoization with dictionary
# O(m + n) Space complexity => max stack depth of m + n

print(grid_traveller(1, 1)) # 1
print(grid_traveller(3, 1)) # 1
print(grid_traveller(2, 3)) # 3
print(grid_traveller(3, 2)) # 3
print(grid_traveller(3, 3)) # 6
print(grid_travellero(1, 1)) # 1
print(grid_travellero(3, 1)) # 1
print(grid_travellero(2, 3)) # 3
print(grid_travellero(3, 2)) # 3
print(grid_travellero(3, 3)) # 3
print(grid_travellero(20, 20)) # 35345263800
