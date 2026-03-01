# Leetcode 221. Maximal Square

# https://leetcode.com/problems/maximal-square/description/

# Tags -> Array, Dynamic Programming, Matrix

def max_square(matrix):
    if not matrix or not matrix[0]:
        return 0

    r, c = len(matrix), len(matrix[0])
    table = [[0] * (c + 1) for _ in range(r + 1)]
    max_side = 0

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if matrix[i - 1][j - 1] == 1:
                table[i][j] = 1 + min(
                    table[i - 1][j],     # top
                    table[i][j - 1],     # left
                    table[i - 1][j - 1]  # top-left
                )
                max_side = max(max_side, table[i][j])
    return max_side * max_side

# Let r, c = len(matrix), len(matrix[0])
# O(r * c) - Time complexity
# O(r* c) - Space complexity

print(max_square([["1","0","1","0","0"],
                  ["1","0","1","1","1"],["1","1","1","1","1"],
                  ["1","0","0","1","0"]])) # 4
print(max_square([["0","1"],["1","0"]])) # 1
print(max_square([["0"]])) # 0
