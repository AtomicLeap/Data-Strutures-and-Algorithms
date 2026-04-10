# Leetcode 3740. Minimum Distance Between Three Equal Elements I

# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/

# Tags -> Array, Hash Table

from collections import defaultdict

def minimum_distance(nums: list[int]) -> int:
    positions = defaultdict(list)

    for i, num in enumerate(nums):
        positions[num].append(i)

    result = float("inf")

    for idxs in positions.values():
        if len(idxs) < 3:
            continue

        for i in range(2, len(idxs)):
            result = min(result, 2 * (idxs[i] - idxs[i - 2]))

    return -1 if result == float("inf") else result

# O(n) Time complexity - we traverse the list once to build the positions and then check each number's positions
# O(n) Space complexity - in the worst case, all numbers are the same and we store all their positions


print(minimum_distance([1, 2, 3, 1, 2, 3, 1])) # 4
print(minimum_distance([1,2,1,1,3])) # 6
print(minimum_distance([1,1,2,3,2,1,2])) # 8
print(minimum_distance([1])) # -1