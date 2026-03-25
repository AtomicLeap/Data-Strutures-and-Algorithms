# Leetcode 3546. Equal Sum Grid Partition I

# https://leetcode.com/problems/equal-sum-grid-partition-i/description/

# Tags -> Array, Matrix, Enumeration, Prefix Sum

def can_partition_grid(grid: list[list[int]]) -> bool:
    m, n = len(grid), len(grid[0])
    total_sum = sum(grid[r][c] for r in range(m) for c in range(n))

    # If total sum is odd, we can't partition into two equal sums
    if total_sum % 2:
        return False

    target = total_sum // 2

    # Check if we can partition by rows
    curr = 0
    for r in range(m):
        for c in range(n):
            curr += grid[r][c]
        if curr == target:
            return True

    # Check if we can partition by columns
    curr = 0
    for c in range(n):
        for r in range(m):
            curr += grid[r][c]
        if curr == target:
            return True

    return False

# O(m * n) - Time complexity, due to prefix sum computation and enumeration
# O(1) - Space complexity, due to prefix sum matrix

print(can_partition_grid([[1, 4], [2, 3]])) # True
print(can_partition_grid([[1, 3], [2, 4]])) # False
print(can_partition_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # True
