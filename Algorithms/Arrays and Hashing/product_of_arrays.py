# Leetcode 238. Product of Array Except Self

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? 
(The output array does not count as extra space for space complexity analysis.)
"""

# Without using division operator
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [1] * n

    # prefix products
    for i in range(1, n):
        ans[i] = ans[i - 1] * nums[i - 1]

    # suffix products on the fly
    suf = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= suf
        suf *= nums[i]

    return ans

# O(n) Time complexity
# O(1) Space complexity 

# Examples
print(product_except_self([1,2,3,4]))        # [24, 12, 8, 6]
print(product_except_self([-1,1,0,-3,3]))    # [0, 0, 9, 0, 0]


# Using division operator
def product_except_self_division(nums: list[int]) -> list[int]:
    zero_count = nums.count(0)
    if zero_count > 1:
        return [0] * len(nums)

    # product of non-zero elements
    prod = 1
    for x in nums:
        if x != 0:
            prod *= x

    if zero_count == 1:
        # only the index with zero gets prod; others 0
        return [prod if x == 0 else 0 for x in nums]

    # no zeros: safe to divide
    # use integer division; it's exact since nums[i] divides prod
    return [prod // x for x in nums]

# O(n) Time complexity
# O(1) Space complexity 

# Examples
print(product_except_self_division([1,2,3,4]))        # [24, 12, 8, 6]
print(product_except_self_division([-1,1,0,-3,3]))    # [0, 0, 9, 0, 0]