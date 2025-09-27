# Leetcode 268. Missing Number

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only 
number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing
 number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing
number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing
number in the range since it does not appear in nums.
"""

# There are three ways to solve this problem:

# 1 XOR trick (no overflow risk)
# Idea: XOR all indices [0..n] and all values. Equal numbers cancel out, leaving the missing one.
def missing_number(nums):
    n = len(nums)
    x = 0
    for i in range(n + 1):  # XOR all 0..n
        x ^= i
    for v in nums:          # XOR all values
        x ^= v
    return x

# O(n) - Time complexity
# O(1) - Space complexity

# 2 Gauss sum formula
# Sum 0..n and subtract the array sum.
def missing_number_2(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)

# O(n) - Time complexity
# O(1) - Space complexity

# 3 In-place parity XOR (single pass variant)
# Combine both XORs in one loop:
def missing_number_3(nums):
    n = len(nums)
    x = n
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x

# O(n) - Time complexity
# O(1) - Space complexity

print(missing_number([0,1])) # 2
print(missing_number([3,0,1])) # 2
print(missing_number([9,6,4,2,3,5,7,0,1])) # 8

print(missing_number_2([0,1])) # 2
print(missing_number_2([3,0,1])) # 2
print(missing_number_2([9,6,4,2,3,5,7,0,1])) # 8

print(missing_number_3([0,1])) # 2
print(missing_number_3([3,0,1])) # 2
print(missing_number_3([9,6,4,2,3,5,7,0,1])) # 8