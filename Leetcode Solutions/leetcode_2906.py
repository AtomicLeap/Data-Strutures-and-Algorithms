# Leetcode 2906. Construct Product Matrix

# https://leetcode.com/problems/construct-product-matrix/description/

# Tags -> Array, Matrix, Prefix Sum

def construct_product_matrix(grid: list[list[int]]) -> list[list[int]]:
    MOD = 12345
    m, n = len(grid), len(grid[0])
    prefix = [1] * (m * n)
    suffix = [1] * (m * n)

    # Flatten grid
    flat_grid = [grid[r][c] for r in range(m) for c in range(n)]

    # First pass: prefix products
    for i in range(1, m * n):
        prefix[i] = (prefix[i - 1] * flat_grid[i - 1]) % MOD
    
    # Second pass: suffix products
    for i in range(m * n - 2, -1, -1):
        suffix[i] = (suffix[i + 1] * flat_grid[i + 1]) % MOD

    # Combine prefix and suffix products into output matrix
    table = [[1] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            table[r][c] = (prefix[r * n + c] * suffix[r * n + c]) % MOD
    
    return table

# O(n * m) - Time complexity
# O(n * m) - Space complexity, due to prefix and suffix arrays

print(construct_product_matrix([[1, 2], [3, 4]])) # [[24, 12], [8, 6]]
print(construct_product_matrix([[12345],[2],[1]])) # [[2],[0],[0]]

def construct_product_matrix_i(grid: list[list[int]]) -> list[list[int]]:
    MOD = 12345
    m, n = len(grid), len(grid[0])

    # Output matrix; first pass will store prefix products
    table = [[1] * n for _ in range(m)]

    # First pass: prefix products
    prefix = 1
    for r in range(m):
        for c in range(n):
            table[r][c] = prefix
            prefix = (prefix * grid[r][c]) % MOD

    # Second pass: suffix products and combine with prefix products
    suffix = 1
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            table[r][c] = (suffix * table[r][c]) % MOD
            suffix = (suffix * grid[r][c]) % MOD

    return table

# O(n * m) - Time complexity
# O(1) - Extra space, besides the output

print(construct_product_matrix_i([[1, 2], [3, 4]])) # [[24, 12], [8, 6]]
print(construct_product_matrix_i([[12345],[2],[1]])) # [[2],[0],[0]]

def construct_product_matrix_o(grid: list[list[int]]) -> list[list[int]]:
    MOD = 12345
    m, n = len(grid), len(grid[0])

    # Output matrix; first pass will store prefix products
    table = [[1] * n for _ in range(m)]

    # First pass: prefix products
    prefix = 1
    for k in range(m * n):
        r, c = divmod(k, n)
        table[r][c] = prefix
        prefix = (prefix * grid[r][c]) % MOD

    # Second pass: suffix products
    suffix = 1
    for k in range(m * n - 1, -1, -1):
        r, c = divmod(k, n)
        table[r][c] = (table[r][c] * suffix) % MOD
        suffix = (suffix * grid[r][c]) % MOD

    return table

# O(n * m) - Time complexity
# O(1) - Extra space, besides the output

print(construct_product_matrix_o([[1, 2], [3, 4]])) # [[24, 12], [8, 6]]
print(construct_product_matrix_o([[12345],[2],[1]])) # [[2],[0],[0]]
