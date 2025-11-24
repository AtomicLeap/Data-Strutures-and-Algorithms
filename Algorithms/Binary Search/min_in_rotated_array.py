# Leetcode 153. Find Minimum in Rotated Sorted Array

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Idea
# In a rotated sorted array with unique numbers, at least one half is sorted.
# Compare the middle element to the rightmost element:
# If nums[mid] > nums[right], the minimum is to the right of mid → set left = mid + 1.
# Otherwise, the minimum is at mid or to the left → set right = mid.
# Loop until left == right; that index is the minimum.
# This works even if the array is not rotated (already sorted); the search converges to index 0.
def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# O(log n) - Time complexity
# O(1) - Space complexity

print(find_min([3,4,5,1,2])) # 1
print(find_min([4,5,6,7,0,1,2])) # 0
print(find_min([11,13,15,17])) # 11