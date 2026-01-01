# Leetcode 136. Single Number

# https://leetcode.com/problems/single-number/description/

# Use XOR (^)

def single_number(nums: list[int]) -> int:
    results = 0

    for num in nums:
        results ^= num
    return results

# O(n) Time complexity
# O(1) Space complexity


print(single_number([2,2,1])) # 1
print(single_number([4,1,2,1,2])) # 4
print(single_number([1])) # 1

