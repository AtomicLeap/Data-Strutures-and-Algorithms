# Leetcode 3661. Maximum Walls Destroyed by Robots

# https://leetcode.com/problems/maximum-walls-destroyed-by-robots/description

# Tags ->  Binary Search, Dynamic Programming, Hard

from bisect import bisect_left, bisect_right
from math import inf


def max_walls(robots: list[int], distance: list[int], walls: list[int]) -> int:
    walls.sort()

    def count(l, r):
        if l > r:
            return 0
        return bisect_right(walls, r) - bisect_left(walls, l)

    n = len(robots)

    arr = []
    for i in range(n):
        arr.append([robots[i], distance[i]])
    arr.sort()
    arr.append([inf, 0])  # sentinel

    table = [[0] * 2 for _ in range(n + 1)]

    # first robot shoots left
    table[0][1] = count(arr[0][0] - arr[0][1], arr[0][0])

    for i in range(n):
        l, ld = arr[i]
        r, rd = arr[i + 1]

        # robot at l shoots right
        left1, right1 = l, min(l + ld, r - 1)

        # robot at r shoots left
        left2, right2 = max(r - rd, l + 1), r

        left_count = count(left1, right1)
        right_count = count(left2, right2)
        both_count = left_count + right_count - count(max(left1, left2), min(right1, right2))

        table[i + 1][0] = max(
            table[i][0] + left_count,
            table[i][1]
        )

        table[i + 1][1] = max(
            table[i][1] + right_count,
            table[i][0] + both_count
        )

    return max(table[n][0], table[n][1])
    
# O(n log n + m log m) - Time complexity
# O(n + m) - Space complexity

print(max_walls([4], [3], [1, 10]))  # Output: 1
print(max_walls([10, 2], [5, 1], [5, 2, 7]))  # Output: 3
print(max_walls([1, 2], [100, 1], [10]))  # Output: 0