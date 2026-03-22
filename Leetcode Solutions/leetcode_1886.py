# Leetcode 1886. Determine Whether Matrix Can Be Obtained By Rotation

# https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

# Tags -> Matrix, Simulation, Array 

# Idea
"""
Key rotation rule

For an n x n matrix, a 90° clockwise rotation maps:
- Element at (i, j) moves to (j, n - 1 - i)
    rotated[j][n - 1 - i] = matrix[i][j]

To determine if one matrix can be obtained by rotating another, we can:
1. Rotate the first matrix up to 4 times (0°, 90°, 180°, 270°).
2. After each rotation, check if the rotated matrix matches the target matrix. 
3. If a match is found at any rotation, return True. If no match is 
    found after all rotations, return False.
"""


def find_rotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    def rotate(matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)
        rotated = [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                rotated[col][n - 1 - row] = matrix[row][col]
        return rotated

    for _ in range(4):
        if mat == target:
            return True
        mat = rotate(mat)

    return False

# O(n^2) Time complexity
# O(n^2) Space complexity

print(find_rotation([[0,1],[1,0]], [[1,0],[0,1]])) # True
print(find_rotation([[0,1],[1,1]], [[1,0],[0,1]])) # False
print(find_rotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]])) # True   


def find_rotation_i(mat: list[list[int]], target: list[list[int]]) -> bool:
    for _ in range(4):
        if mat == target:
            return True
        mat = [list(reversed(col)) for col in zip(*mat)]
    return False
    
# O(n^2) Time complexity
# O(1) Space complexity
 
print(find_rotation_i([[0,1],[1,0]], [[1,0],[0,1]])) # True
print(find_rotation_i([[0,1],[1,1]], [[1,0],[0,1]])) # False
print(find_rotation_i([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]])) # True   

