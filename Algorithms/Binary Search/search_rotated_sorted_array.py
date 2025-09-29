# Leetcode 33. Search in Rotated Sorted Array

"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly left rotated at an unknown 
index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], 
..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] 
might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

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
