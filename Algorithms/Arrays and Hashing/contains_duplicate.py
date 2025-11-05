# Leetcode 217. Contains Duplicate

# https://leetcode.com/problems/contains-duplicate/description/

def has_duplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)

print(has_duplicate([1, 2, 3, 3])) # True
print(has_duplicate([1, 2, 3, 4, 5])) # False