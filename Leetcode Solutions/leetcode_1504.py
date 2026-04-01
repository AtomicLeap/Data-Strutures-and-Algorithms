# Leetcode 1504. Count Submatrices With All Ones

# https://leetcode.com/problems/count-submatrices-with-all-ones/description/

# Tags -> Stack, Matrix

def num_submatrices(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    result = 0

    for r in range(m):
        # Build histogram for current row
        for c in range(n):
            if matrix[r][c] == 1:
                heights[c] += 1
            else:
                heights[c] = 0

        stack = []
        count_table = [0] * n
        for c in range(n):
            while stack and heights[stack[-1]] >= heights[c]:
                stack.pop()

            if stack:
                prev_index = stack[-1]
                count_table[c] = count_table[prev_index] + heights[c] * (c - prev_index)
            else:
                count_table[c] = heights[c] * (c + 1)

            stack.append(c)
            result += count_table[c]

    return result

# O(m * n) Time complexity, where m and n are the dimensions of the matrix
# O(n) Space complexity

print(num_submatrices([[1,0,1],[1,1,0],[1,1,0]])) # 13
print(num_submatrices([[0,1,1,0],[0,1,1,1],[1,1,1,0]])) # 24
print(num_submatrices([[1,1,1,1,1,1]])) # 21
print(num_submatrices([[1,0,1],[0,1,0],[1,0,1]])) # 5
print(num_submatrices([[0,1,1,0],[0,1,1,1],[1,1,1,0]])) # 24

