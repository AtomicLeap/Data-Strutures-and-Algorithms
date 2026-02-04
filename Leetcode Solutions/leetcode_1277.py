# Leetcode 1277. Count Square Submatrices with All Ones

 # https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

def solution(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    total = 0

    # First row and first column stay as-is (0 or 1), already represent dp values
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and i > 0 and j > 0:
                matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
            # add dp[i][j] to total
            total += matrix[i][j]
    return total

print(solution([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))

print(solution([
  [1,0,1],
  [1,1,0],
  [1,1,0]
]))

# Let m, n = len(matrix), len(matrix[0])
# O(m . n) - Time complexity
# O(m . n) - Space complexity