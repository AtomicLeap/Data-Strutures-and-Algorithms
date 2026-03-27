# Leetcode 2946. Matrix Similarity After Cyclic Shifts

# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/description

# Tags -> Array, Math, Matrix, Simulation

def are_cyclic_matrix_similar(matrix: list[list[int]], k: int) -> bool:
    m, n = len(matrix), len(matrix[0])
    shift = k % n

    for r in range(m):
        for c in range(n):
            if r % 2 == 0:
                # even row: shifted left
                if matrix[r][c] != matrix[r][(c + shift) % n]:
                    return False
            else:
                # odd row: shifted right
                if matrix[r][c] != matrix[r][(c - shift) % n]:
                    return False

    return True

# O(m * n) - Time complexity
# O(1) - Space complexity

print(are_cyclic_matrix_similar([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4)) # False
print(are_cyclic_matrix_similar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2)) # True
print(are_cyclic_matrix_similar([[2,2],[2,2]], 3)) # True