# Leetcode 3548. Equal Sum Grid Partition II

# https://leetcode.com/problems/equal-sum-grid-partition-ii/description/

# Tags -> Array, Matrix, Enumeration, Prefix Sum

def can_partition_grid(grid: list[list[int]]) -> bool:
    def check_partition(g):
        rows = len(g)
        cols = len(g[0])

        curr = 0
        seen = {}  # value -> [first_position, last_position]

        for i in range(rows - 1):  # cut after row i
            for j in range(cols):
                v = g[i][j]
                curr += v

                if v in seen:
                    seen[v][1] = (i, j)
                else:
                    seen[v] = [(i, j), (i, j)]

            diff = total - 2 * curr

            # exact match
            if diff == 0:
                return True

            # need to remove one cell of value = -diff (from top part)
            if -diff in seen:
                (fr, fc), (lr, lc) = seen[-diff]

                # case 1: general rectangle (>= 2x2)
                if cols > 1 and i + 1 > 1:
                    return True

                # case 2: single row
                if i + 1 == 1 and cols > 1:
                    if fc == 0 or lc == cols - 1:
                        return True

                # case 3: single column
                if cols == 1:
                    if fr == 0 or lr == i:
                        return True

        return False

    n = len(grid)
    m = len(grid[0])

    total = sum(grid[i][j] for i in range(n) for j in range(m))

    # horizontal cuts
    if check_partition(grid) or check_partition(grid[::-1]):
        return True

    # vertical cuts via transpose
    grid = list(zip(*grid))

    if check_partition(grid) or check_partition(grid[::-1]):
        return True

    return False

# O(m * n) - Time complexity, due to prefix sum computation and enumeration
# O(1) - Space complexity, due to prefix sum matrix

print(can_partition_grid([[1,4],[2,3]])) # True
print(can_partition_grid([[1,2],[3,4]])) # True
print(can_partition_grid([[1,2,4],[2,3,5]])) # False
print(can_partition_grid([[4,1,8],[3,2,6]])) # False
