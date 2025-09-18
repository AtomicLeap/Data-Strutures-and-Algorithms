# Leetcode 15. 3Sum

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 
Constraints:
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # Optional minor pruning: since array is sorted, if nums[i] > 0, sum can't be 0
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            sum_total = nums[i] + nums[left] + nums[right]
            if sum_total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Move both pointers and skip duplicates
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum_total < 0:
                left += 1
            else:
                right -= 1

    return result


# n = len(nums)
# O(n^2) - Time complexity -> Sorting O(n log n) + two-pointer scan O(n²) ⇒ overall O(n²) time;
#  O(1) - Space complexity ->  O(1) extra space (excluding output - result).

print(three_sum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(three_sum([0,1,1])) # []
print(three_sum([0,0,0])) # [[0,0,0]]