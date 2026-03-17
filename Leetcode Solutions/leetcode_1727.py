# Leetcode 1727. Largest Submatrix With Rearrangements

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description

# Tags -> Greedy, Array

def largest_submatrix(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    result = 0

    for row in range(m):
        # Update histogram heights
        for col in range(n):
            if matrix[row][col] == 1:
                heights[col] += 1
            else:
                heights[col] = 0

        # Reorder columns optimally for this row
        sorted_heights = sorted(heights, reverse=True)

        # Try every possible width
        for i, height in enumerate(sorted_heights):
            result = max(result, height * (i + 1))

    return result

# O(m * n log n) - Time complexity
# O(n) - Space complexity

print(largest_submatrix([[0,0,1],[1,1,1],[1,0,1]])) # 4
print(largest_submatrix([[1,0,1,0,1]])) # 3
print(largest_submatrix([[1,1,0],[1,0,1]])) # 2
