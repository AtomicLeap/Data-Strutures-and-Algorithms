# Leetcode 1536. Minimum Swaps to Arrange a Binary Grid

# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description

# Tags -> Greedy, Matrix, Array

def min_swaps(grid: list[list[int]]) -> int:
    n = len(grid)

    # trailing zeros in row i
    trailing_zeroes = []
    for row in range(n):
        count = 0
        for col in range(n - 1, -1, -1):
            if grid[row][col] == 0:
                count += 1
            else:
                break
        trailing_zeroes.append(count)

    swaps = 0

    for i in range(n):
        need = n - 1 - i

        # find first row j >= i with trailing_zeroes[j] >= need
        j = i
        while j < n and trailing_zeroes[j] < need:
            j += 1

        if j == n:
            return -1

        # bubble row j up to i
        while j > i:
            trailing_zeroes[j], trailing_zeroes[j - 1] = trailing_zeroes[j - 1], trailing_zeroes[j]
            swaps += 1
            j -= 1

    return swaps

# O(n^2) - Time complexity
# O (n) - Space complexity

print(min_swaps([[0,0,1],[1,1,0],[1,0,0]])) # 3
print(min_swaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]])) # -1
print(min_swaps([[1,0,0],[1,1,0],[1,1,1]])) # 0
