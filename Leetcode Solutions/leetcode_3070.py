# Leetcode 3070. Count Submatrices with Top-Left Element and Sum Less Than k

# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/

# Tags -> Array, Prefix Sum

def count_submatrices(grid: list[list[int]], k: int) -> int:
    m, n = len(grid), len(grid[0])
    result = 0

    # Build 2D prefix sums in-place inside grid
    for row in range(m):
        for col in range(n):
            top = grid[row - 1][col] if row > 0 else 0
            left = grid[row][col - 1] if col > 0 else 0
            diag = grid[row - 1][col - 1] if row > 0 and col > 0 else 0

            grid[row][col] = grid[row][col] + top + left - diag

            if grid[row][col] <= k:
                result += 1

    return result

# O(m . n) - Time complexity
# O(1) - Space complexity

print(count_submatrices([[7,6,3],[6,6,1]], 18)) # 4
print(count_submatrices([[7,2,9],[1,5,0],[2,6,6]], 20)) # 6