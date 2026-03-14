# Leetcode 875. Koko Eating Bananas

# https://leetcode.com/problems/koko-eating-bananas/description/

# Tags -> Binary Search

# Idea
"""
Hours = Piles/k

Mathematical ceiling division trick: (pile + k - 1) // k 
"""

def min_eating_speed(piles: list[int], h: int) -> int:
    def can_finish_bananas(k: int):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k   # ceil(pile / k)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2

        if can_finish_bananas(mid):
            right = mid
        else:
            left = mid + 1

    return left

# O(n · log n) - Time complexity
# O(1) - Space complexity

print(min_eating_speed([3,6,7,11], 8)) # 4
print(min_eating_speed([30,11,23,4,20], 5)) # 30
print(min_eating_speed([30,11,23,4,20], 6)) # 23