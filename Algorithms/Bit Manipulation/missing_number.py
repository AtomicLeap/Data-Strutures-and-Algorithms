# Leetcode 268. Missing Number

# https://leetcode.com/problems/missing-number/description/

# There are three ways to solve this problem:

# 1. XOR trick (no overflow risk)
# Idea: XOR all indices [0..n] and all values. Equal numbers cancel out, leaving the missing one.
def missing_number(nums):
    n = len(nums)
    result = 0 # Zero is Identity for XOR
    for idx in range(n + 1):  # XOR all 0..n
        result ^= idx
    for num in nums:          # XOR all values
        result ^= num
    return result

# O(n) - Time complexity
# O(1) - Space complexity

# 2. Gauss sum formula --> S = n * (n + 1) // 2
# Sum 0..n and subtract the array sum.
def missing_number_2(nums):
    n = len(nums)
    full_sum = n * (n + 1) // 2
    return full_sum - sum(nums)

# O(n) - Time complexity
# O(1) - Space complexity

# 3 In-place parity XOR (single pass variant)
# Combine both XORs in one loop:
def missing_number_3(nums):
    n = len(nums)
    result = n
    for idx, num in enumerate(nums):
        result ^= idx ^ num
    return result

# O(n) - Time complexity
# O(1) - Space complexity

print(missing_number([0,1])) # 2
print(missing_number([3,0,1])) # 2
print(missing_number([9,6,4,2,3,5,7,0,1])) # 8
print('-----------------------------------------')
print(missing_number_2([0,1])) # 2
print(missing_number_2([3,0,1])) # 2
print(missing_number_2([9,6,4,2,3,5,7,0,1])) # 8
print('-----------------------------------------')
print(missing_number_3([0,1])) # 2
print(missing_number_3([3,0,1])) # 2
print(missing_number_3([9,6,4,2,3,5,7,0,1])) # 8