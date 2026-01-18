# Leetcode 1929. Concatenation of Array

# https://leetcode.com/problems/concatenation-of-array/description/

def array_concatenation(nums: list[int]) -> list[int]:
    return nums.extend(nums)

print(array_concatenation([1,2,1])) # [1,2,1,1,2,1]
print(array_concatenation([1,3,2,1])) # [1,3,2,1,1,3,2,1]

# O(n) Time complexity
# O(1) Space complexity
