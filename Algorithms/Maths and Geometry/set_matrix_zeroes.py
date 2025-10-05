# Leetcode 73. Set Matrix Zeroes

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 
Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 
Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# Idea (constant space)
# Scan first row/col to see if they themselves need to be zeroed (first_row_zero, first_col_zero).
# For each cell (i, j) with i>0, j>0, if matrix[i][j] == 0, mark its row and column by setting matrix[i][0] = 0 and matrix[0][j] = 0.
# Second pass over the inner submatrix: for each (i, j) with i>0, j>0, set to 0 if its row or column is marked (i.e., matrix[i][0]==0 or matrix[0][j]==0).
# Finally zero the first row/col if the initial flags were set.

def set_matrix_zeroes(matrix):
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])

    # Step 1: check if first row/col need to be zeroed
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Step 2: use first row/col as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Step 3: zero cells based on markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 4: zero first row if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Step 5: zero first column if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0

    return matrix

print(set_matrix_zeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(set_matrix_zeroes([[1,1,1],[1,0,1],[1,1,1]])) # [[1,0,1],[0,0,0],[1,0,1]]

# O( m * n) - Time complexity
# O(1) - Space complexity