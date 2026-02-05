# Leetcode 3379. Transformed Array

# https://leetcode.com/problems/transformed-array/description

# Key Idea
"""
Let n = len(nums)

For each i:

If nums[i] == 0: result[i] = 0

Else: j = (i + nums[i]) % n, result[i] = nums[j]

Mathematical idea of modulo
Modulo is defined so that for any integers a and positive n:
    a % n = r <-> a = q.n + r,    where 0 <= r < n
q is an integer (the quotient)
r is the remainder

The key rule is that the remainder is always non-negative.
Example:
1. -1 % 4 = 3   -> -1 = (-1)* 4 + 3
"""

def construct_transformed_array(nums: list[int]) -> list[int]:
    n = len(nums)
    results = [0] * n

    for i in range(n):
        if nums[i] == 0:
            results[i] = 0
        else:
            idx = (i + nums[i]) % n
            results[i] = nums[idx]
    return results

# O(n) - Time complexity
# O(n) - Space complexity

print(construct_transformed_array([3,-2,1,1])) # [1,1,1,3]
print(construct_transformed_array([-1,4,-1])) # [-1,-1,4]
