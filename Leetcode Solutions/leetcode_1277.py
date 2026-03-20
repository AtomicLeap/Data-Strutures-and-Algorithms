# Leetcode 1277. Count Square Submatrices with All Ones

# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

# Tags -> Dynamic Programming, Array

def solution(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    total = 0 # total of cells with ones "1"

    # First row and first column stay as-is (0 or 1), already represent dp values
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 1 and row > 0 and col > 0:
                matrix[row][col] = 1 + min(matrix[row-1][col], matrix[row][col-1], matrix[row-1][col-1])
            # add matrix[row][col] to total
            total += matrix[row][col]
    return total

print(solution([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])) # 15

print(solution([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])) # 7

# Let m, n = len(matrix), len(matrix[0])
# O(m . n) - Time complexity
# O(m . n) - Space complexity