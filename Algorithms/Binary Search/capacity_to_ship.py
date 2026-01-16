# 1011. Capacity To Ship Packages Within D Days

# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# Idea
"""
1. Design a condition function, let's call it feasible, given an input capacity, 
    it returns whether it's possible to ship all packages within D days. 
    This can run in a greedy way: if there's still room for the current package, 
    we put this package onto the conveyor belt, otherwise we wait for the next day 
    to place this package. If the total days needed exceeds D, we return False, 
    otherwise we return True.
2. Capacity should be at least max(weights), otherwise the conveyor belt couldn't 
    ship the heaviest package. On the other hand, capacity need not be more than 
    sum(weights), because then we can ship all packages in just one day.
"""

def ship_within_days(weights: list[int], days: int) -> int:
    def feasible(capacity: int) -> bool:
        days_count = 1
        total_weight = 0
        for weight in weights:
            total_weight += weight
            if total_weight > capacity:  # too heavy, wait for the next day
                total_weight = weight
                days_count += 1
                if days_count > days:  # cannot ship within D days
                    return False
        return True

    left, right = max(weights), sum(weights) # min_limit, max_limit for daily weight capacity
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left

# O(n) - Time complexity
# O(1) - Space complexity

print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5)) # 15
print(ship_within_days([3,2,2,4,1,4], 3)) # 6
print(ship_within_days([1,2,3,1,1], 4)) # 3
