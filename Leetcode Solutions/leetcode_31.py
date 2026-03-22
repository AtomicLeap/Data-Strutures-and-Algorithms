# Leetcode 31. Next Permutation

# https://leetcode.com/problems/next-permutation/

# Tags -> Two Pointers, Array

def next_permutation(nums: list[int]) -> None:
    """
    Modifies nums in-place to become its next permutation.
    """
    n = len(nums)

    # 1. Find the first index from the right where nums[i] < nums[i + 1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # 2. If such index exists, find the rightmost number greater than nums[i]
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # 3. Reverse the suffix starting at i + 1
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# O(n) Time complexity
# O(1) Space complexity 


next_permutation([1,2,3]) # [1,3,2]
next_permutation([3,2,1]) # [1,2,3]
next_permutation([1,1,5]) # [1,5,1]
