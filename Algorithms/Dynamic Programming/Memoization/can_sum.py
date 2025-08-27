# can sum problem

"""
Write a function "can_sum(target, nums)" that takes a target 
and an array of numbers as arguements. The function should 
return a boolean indicating whether or not it is possible 
to generate the target sum using numbers from the array.

Constraints
You may use an element of the array as many times as needed.
You may assume that all input numbers are non-negative.
"""

# Brute force solution
def can_sum(target: int, nums: list[int]) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        remainder = target - num
        if (can_sum(remainder, nums)):
            return True
    return False
# m = size of target
# n = len(nums)
# O(n^m) Time complexity
# O(m) Space complexity => max stack depth of m

# Optimized solution
def can_sum(target: int, nums: list[int]) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        remainder = target - num
        if (can_sum(remainder, nums)):
            return True
    return False
# m = size of target
# n = len(nums)
# O(n^m) Time complexity
# O(m) Space complexity => max stack depth of m

# Optimized solution
def can_sumo(target: int, nums: list[int], memo: dict = {}) -> bool:
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in nums:
        remainder = target - num
        if can_sumo(remainder, nums, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False
# m = size of target
# n = len(nums)
# O(m * n) Time complexity
# O(m) Space complexity => max stack depth of m

print(can_sum(7, [2, 4]))
print(can_sum(23, [2, 7, 4, 5]))
print(can_sum(18, [2, 3, 4, 5]))

print(can_sumo(7, [2, 4]))
print(can_sumo(23, [2, 7, 4, 5]))
print(can_sumo(18, [2, 3, 4, 5]))
print(can_sumo(30, [7, 11, 14]))
print(can_sumo(301, [11]))
print(can_sumo(93, [7, 9, 5, 14]))
