# Leetcode 33. Search in Rotated Sorted Array

# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Idea
# This exploits the fact that in a rotated sorted array with unique numbers, at least one half is always sorted.
# At each step:
# Compute mid.
# If nums[mid] == target, return mid.
# Determine which side is sorted:
# If nums[l] <= nums[mid], the left half [l..mid] is sorted.
# If target lies in [nums[l], nums[mid]], move right pointer to mid - 1; else move left pointer to mid + 1.
# Else the right half [mid..r] is sorted.
# If target lies in [nums[mid], nums[r]], move left pointer to mid + 1; else move right pointer to mid - 1.
# If we exit the loop, return -1.

def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # Left half sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# O(log n) - Time complexity
# O(1) - Space complexity

print(search_rotated_array([4,5,6,7,0,1,2], 0)) # 4
print(search_rotated_array([4,5,6,7,0,1,2], 3)) # -1
print(search_rotated_array([1], 0)) # -1
