# Leetcode 3567. Minimum Absolute Difference in Sliding Submatrix

# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/description/

# Tags -> Matrix, Array

# Idea
"""
For each k x k submatrix:

1. collect all values,
2. keep only the unique values,
3. sort them,
4. the minimum absolute difference must occur between adjacent values in 
    sorted order.

That gives a straightforward solution that is easily fast enough for m, n <= 30.
"""

def min_abs_diff(grid: list[list[int]], k: int) -> list[list[int]]:
    m, n = len(grid), len(grid[0])
    rows = m - k + 1
    cols = n - k + 1
    result = [[0] * cols for _ in range(rows)]

    for top in range(rows):
        for left in range(cols):
            values = set()

            # Collect all values in the current k x k submatrix
            for i in range(top, top + k):
                for j in range(left, left + k):
                    values.add(grid[i][j])

            # If there is only one distinct value, answer is 0
            if len(values) <= 1:
                result[top][left] = 0
                continue

            # Sort distinct values and compute min adjacent difference
            sorted_vals = sorted(values)
            best = float('inf')

            for i in range(1, len(sorted_vals)):
                best = min(best, sorted_vals[i] - sorted_vals[i - 1])

            result[top][left] = best

    return result

# Time complexity
"""
Let each window contain k^2 cells.

For each window:
-> collecting values: O(k^2)
-> sorting distinct values: at most O(k^2 log(k^2))

total complexity -> O((m -k + 1)(n - k + 1). k^2. log (k^2))
"""

# O(k^2) - Space complexity

print(min_abs_diff([[1,8],[3,-2]], 2)) # [[2]]
print(min_abs_diff([[3,-1]], 1)) # [[0, 0]]
print(min_abs_diff([[1,-2,3],[2,3,5]], 2)) # [[1, 2]]