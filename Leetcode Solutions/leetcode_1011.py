# Leetcode 1011. Capacity To Ship Packages Within D Days

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# Tags -> Binary Search


def ship_within_days(weights: list[int], days: int) -> int:
    n = len(weights)
    def enough_capacity(capacity: int) -> bool:
        idx = 0
        for _ in range(days):
            curr_capacity = capacity
            while idx < n and curr_capacity >= weights[idx]:
                curr_capacity -= weights[idx]
                idx += 1

                if idx == n:
                    return True
        return False

    left, right = max(weights), sum(weights) # min_limit, max_limit for daily weight capacity
    while left < right:
        mid = left + (right - left) // 2
        if enough_capacity(mid):
            right = mid
        else:
            left = mid + 1
    return left

# O(n) - Time complexity
# O(1) - Space complexity

print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5)) # 15
print(ship_within_days([3,2,2,4,1,4], 3)) # 6
print(ship_within_days([1,2,3,1,1], 4)) # 3