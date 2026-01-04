# 35. Search Insert Position

# https://leetcode.com/problems/search-insert-position/description/


# 1. Use Binary Search Alogorithm (returning the left index if target not found)

# Key Idea
"""
1. We are looking for the minimal k value satisfying nums[k] >= target
2. Also notice that the input target might be larger than all elements in 
    nums and therefore needs to placed at the end of the array. 
    That's why we should initialize right = len(nums) instead of 
    right = len(nums) - 1.
"""

def search_insert_position(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

# O(log n) - Time complexity
# O(1) - Space complexity

# 2. Use bisect built-in function (It uses Binary Search under the hood)

from bisect import bisect_left

def search_insert_position_b(nums: list[int], target: int) -> int:
    return bisect_left(nums, target)

# O(log n) - Time complexity
# O(1) - Space complexity

print(search_insert_position([1,3,5,6], 5)) # 2
print(search_insert_position([1,3,5,6], 2)) # 1
print(search_insert_position([1,3,5,6], 7)) # 4
print('----------------------------------------------')
print(search_insert_position_b([1,3,5,6], 5)) # 2
print(search_insert_position_b([1,3,5,6], 2)) # 1
print(search_insert_position_b([1,3,5,6], 7)) # 4