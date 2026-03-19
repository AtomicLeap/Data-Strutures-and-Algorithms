# Leetcode 3212. Count Submatrices With Equal Frequency of X and Y

# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/description

# Tags -> Array, Matrix, Prefix Sum

def number_of_submatrices(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])

    prefix_sum_x = [[0] * (n + 1) for _ in range(m + 1)]
    prefix_sum_y = [[0] * (n + 1) for _ in range(m + 1)]

    result = 0

    for row in range(1, m + 1):
        for col in range(1, n + 1):
            cell = grid[row - 1][col - 1]

            prefix_sum_x[row][col] = (
                prefix_sum_x[row - 1][col]
                + prefix_sum_x[row][col - 1]
                - prefix_sum_x[row - 1][col - 1]
                + (1 if cell == 'X' else 0)
            )

            prefix_sum_y[row][col] = (
                prefix_sum_y[row - 1][col]
                + prefix_sum_y[row][col - 1]
                - prefix_sum_y[row - 1][col - 1]
                + (1 if cell == 'Y' else 0)
            )

            if prefix_sum_x[row][col] and prefix_sum_x[row][col] == prefix_sum_y[row][col]:
                result += 1

    return result

# O(m . n) - Time complexity
# O(m . n) - Space complexity

print(number_of_submatrices([["X","Y","."],["Y",".","."]])) # 3
print(number_of_submatrices([["X","X"],["X","Y"]])) # 0
print(number_of_submatrices([[".","."],[".","."]])) # 0