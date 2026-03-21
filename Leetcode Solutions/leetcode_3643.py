# Leetcode 3643. Flip Square Submatrix Vertically

# https://leetcode.com/problems/flip-square-submatrix-vertically/description

# Tags -> Two Pointers, Matrix

def reverse_submatrix(grid: list[list[int]], x: int, y: int, k: int) -> List[List[int]]:
    top = x
    bottom = x + k - 1

    while top < bottom:
        for col in range(y, y + k):
            grid[top][col], grid[bottom][col] = grid[bottom][col], grid[top][col]
        top += 1
        bottom -= 1

    return grid


# O(k^2) - Time complexity
# O(1) - Space complexity

print(reverse_submatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3)) # [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]
print(reverse_submatrix([[3,4,2,3],[2,3,4,2]], 0, 0, 2)) # [[3,4,4,2],[2,3,2,3]]
