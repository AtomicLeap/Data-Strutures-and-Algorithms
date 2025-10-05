# Leetcode 54. Spiral Matrix

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

# Idea
# We keep four pointers (top, bottom, left, right) and peel the matrix layer-by-layer.
def spiral_matrix(matrix: list[list[int]]) -> list[int]:
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # left -> right
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # top -> bottom
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            # right -> left
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            # bottom -> top
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result

# O( m * n) - Time complexity
# O(1) - Space complexity

print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
print(spiral_matrix([[1]])) # [1]
print(spiral_matrix([[1,2,3]])) # [1,2,3]             # single row
print(spiral_matrix([[1],[2],[3]])) # [1,2,3]         # single column