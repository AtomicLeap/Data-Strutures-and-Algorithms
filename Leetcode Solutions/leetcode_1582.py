# Leetcode 1582. Special Positions in a Binary Matrix

# https://leetcode.com/problems/special-positions-in-a-binary-matrix/description

# Tags -> Array, Matrix

def num_special(matrix: list[list[int]]) -> int:
    r = len(matrix)
    c = len(matrix[0])
    row_sum = [0] * r
    col_sum = [0] * c
    total_count = 0

    for row in range(r):
        for col in range(c):
            if matrix[row][col] == 1:
                row_sum[row] += 1
                col_sum[col] += 1

    for row in range(r):
        if row_sum[row] != 1:
            continue
        for col in range(c):
            if matrix[row][col] == 1 and col_sum[col] == 1:
                total_count += 1
    return total_count

# Let r, c = len(rows), len(columns)
# O(r . c) - Time complexity
# O (max(r, c)) - Space complexity

print(num_special([[1,0,0],[0,0,1],[1,0,0]])) # 1
print(num_special([[1,0,0],[0,1,0],[0,0,1]])) # 3
