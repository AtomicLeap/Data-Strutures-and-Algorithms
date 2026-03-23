# Leetcode 1594. Maximum Non Negative Product in a Matrix

# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/description/

# Tags -> Dynamic Programming, Matrix      

def max_product_path(grid: list[list[int]]) -> int:
    MOD = 10**9 + 7
    m, n = len(grid), len(grid[0])

    max_table = [[0] * n for _ in range(m)]
    min_table = [[0] * n for _ in range(m)]

    max_table[0][0] = min_table[0][0] = grid[0][0]

    for r in range(m):
        for c in range(n):
            if r == 0 and c == 0:
                continue

            val = grid[r][c]
            candidates = []

            if r > 0:
                candidates.append(max_table[r - 1][c] * val)
                candidates.append(min_table[r - 1][c] * val)

            if c > 0:
                candidates.append(max_table[r][c - 1] * val)
                candidates.append(min_table[r][c - 1] * val)

            max_table[r][c] = max(candidates)
            min_table[r][c] = min(candidates)

    result = max_table[m - 1][n - 1]
    return result % MOD if result >= 0 else -1

# O(m * n) Time complexity, where m and n are the dimensions of the grid
# O(m * n) Space complexity

print(max_product_path([[1,-2,1],[1,-2,1],[3,-4,1]])) # 8
print(max_product_path([[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]])) # -1
print(max_product_path([[1,3],[0,-4]])) # 0
