# Leetcode 62. Unique Paths

# https://leetcode.com/problems/unique-paths/description/

# Use Maths [Combination]
# Combinatorial Solution (O(1) time)
"""
Each path consists of exactly:
1. (m - 1) downs (↓)
2. (n - 1) rights (→)

Total moves = (m - 1) + (n - 1) = (m + n - 2)
You just choose where the downs (or rights) go.

unique_paths = Combination((Total moves), (one of two moves))

unique_paths = Combination(m + n - 2, m - 1) = (m + n - 2)!/((m - 1)!(n - 1)!
"""

import math

def unique_paths_m(m: int, n: int) -> int:
    return math.comb(m + n - 2, m - 1)

# O(1) Time complexity
# O(1) Space complexity


# Iterative solution (Table)

def unique_paths_o(m: int, n: int) -> int:
    table = [1] * n

    for _ in range(1, m):
        for column in range(1, n):
            table[column] += table[column - 1]
    return table[n - 1]

# O(m * n) Time complexity
# O(n) Space complexity

def unique_paths_t(m: int, n: int) -> int:
    table = [[1 for _ in range(n)] for _ in range(m)]

    for row in range(1, m):
        for column in range(1, n):
            table[row][column] = table[row - 1][column] + table[row][column - 1]
    return table[m - 1][n - 1]

# O(m * n) Time complexity
# O(m * n) Space complexity

print(unique_paths_m(3, 7)) # 28
print(unique_paths_m(3, 2)) # 3

print(unique_paths_o(3, 7)) # 28
print(unique_paths_o(3, 2)) # 3

print(unique_paths_t(3, 7)) # 28
print(unique_paths_t(3, 2)) # 3