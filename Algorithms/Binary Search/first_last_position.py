# Leetcode 34. Find First and Last Position of Element in Sorted Array

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

def first_last_position(nums: list[int], target: int) -> list[int]:
    def lower_bound(num: int) -> int:
        low_bound, high_bound = 0, len(nums)

        while low_bound < high_bound:
            mid = (low_bound + high_bound) // 2

            if nums[mid] < num:
                low_bound = mid + 1
            else:
                high_bound = mid
        return low_bound
    
    def higher_bound(num: int) -> int:
        low_bound, high_bound = 0, len(nums)

        while low_bound < high_bound:
            mid = (low_bound + high_bound) // 2

            if nums[mid] <= num:
                low_bound = mid + 1
            else:
                high_bound = mid
        return low_bound
    
    lower_idx = lower_bound(target)
    if lower_idx == len(nums) or nums[lower_idx] != target:
        return [-1, -1]
    
    higher_idx = higher_bound(target) - 1

    return [lower_idx, higher_idx]

# O(log n) - Time complexity
# O(1) - Space complexity

print(first_last_position([5,7,7,8,8,10], 8)) # [3, 4]
print(first_last_position([5,7,7,8,8,10], 6)) # [-1, -1]
print(first_last_position([], 0)) # [-1, -1]
print(first_last_position([1], 1)) # [0, 0]
