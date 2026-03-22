# Leetcode 1482. Minimum Number of Days to Make m Bouquets

# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

# Tags -> Binary Search, Array

def min_days(bloom_day: list[int], m: int, k: int) -> int:
    if m * k > len(bloom_day):
        return -1

    def can_make(days: int) -> bool:
        bouquets = 0
        flowers = 0

        for bloom in bloom_day:
            if bloom <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        return bouquets >= m

    left, right = min(bloom_day), max(bloom_day)

    while left < right:
        mid = (left + right) // 2
        if can_make(mid):
            right = mid
        else:
            left = mid + 1

    return left

# O(n log d) Time complexity, where d is the range of bloom days
# O(1) Space complexity

print(min_days([1,10,3,10,2], 3, 1)) # 3
print(min_days([1,10,3,10,2], 3, 2)) # -1
print(min_days([7,7,7,7,12,7,7], 2, 3)) # 12

