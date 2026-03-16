# Leetcode 1878. Get Biggest Three Rhombus Sums in a Grid

# https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/description

# Tags -> Maths

def get_biggest_three(grid: list[list[int]]) -> list[int]:
    m, n = len(grid), len(grid[0])

    # dr: prefix sums along '\' diagonals
    dr = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            dr[i + 1][j + 1] = dr[i][j] + grid[i][j]

    # dl: prefix sums along '/' diagonals
    dl = [[0] * (n + 2) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n - 1, -1, -1):
            dl[i + 1][j] = dl[i][j + 1] + grid[i][j]

    def diag_dr(r1: int, c1: int, r2: int, c2: int) -> int:
        """Sum on '\' diagonal from (r1,c1) to (r2,c2), inclusive."""
        return dr[r2 + 1][c2 + 1] - dr[r1][c1]

    def diag_dl(r1: int, c1: int, r2: int, c2: int) -> int:
        """Sum on '/' diagonal from (r1,c1) to (r2,c2), inclusive."""
        return dl[r2 + 1][c2] - dl[r1][c1 + 1]

    sums = set()

    for r in range(m):
        for c in range(n):
            # radius 0 rhombus
            sums.add(grid[r][c])

            max_k = min(r, m - 1 - r, c, n - 1 - c)
            for k in range(1, max_k + 1):
                top = (r - k, c)
                right = (r, c + k)
                bottom = (r + k, c)
                left = (r, c - k)

                border = 0
                border += diag_dr(top[0], top[1], right[0], right[1])      # top -> right
                border += diag_dl(right[0], right[1], bottom[0], bottom[1]) # right -> bottom
                border += diag_dr(left[0], left[1], bottom[0], bottom[1])   # left -> bottom
                border += diag_dl(top[0], top[1], left[0], left[1])         # top -> left

                # corners counted twice
                border -= grid[top[0]][top[1]]
                border -= grid[right[0]][right[1]]
                border -= grid[bottom[0]][bottom[1]]
                border -= grid[left[0]][left[1]]

                sums.add(border)

    return sorted(sums, reverse=True)[:3]

# O(m * n * min(m, n)) - Time complexity
# O(m * n) - Space complexity

print(get_biggest_three([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]])) # [228, 216, 211]
print(get_biggest_three([[1,2,3],[4,5,6],[7,8,9]])) # [20,9,8]
print(get_biggest_three([[7,7,7]])) # [7]