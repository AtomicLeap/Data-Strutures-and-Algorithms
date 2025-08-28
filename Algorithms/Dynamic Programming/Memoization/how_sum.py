# can sum problem

"""
Write a function "how_sum(target, nums)" that takes a target 
and an array of numbers as arguements. The function should 
return an array containing any combination of elements that
add up to exactly the target. If there is no combination that 
adds up to the target, then return None.

Constraints
If there are multiple combinations possible, you may return any 
single one. You may assume that all input numbers are non-negative.
"""

# Brute force solution
def how_sum(target: int, numbers: list[int]) -> list[int] | None:
    if target == 0:
        return []
    if target < 0:
        return None
    
    for num in numbers:
        remainder = target - num
        result = how_sum(remainder, numbers)
        if  result != None:
            return result + [num]

    return None
# m = size of target
# n = len(nums)
# O(n^m) Time complexity
# O(m) Space complexity => max stack depth of m

# Optimized solution
def how_sumo(target: int, numbers: list[int], memo: dict = {}) -> list[int] | None:
    if target in memo:
        return memo[target]
    
    if target == 0:
        return []
    if target < 0:
        return None
    
    for num in numbers:
        remainder  = target - num
        result = how_sumo(remainder, numbers, memo)
        if result != None:
            memo[target] = result + [num]
            return memo[target]
    memo[target] = None
    return None
# m = size of target
# n = len(numbers)
# O(m * n) Time complexity
# O(m * m) Space complexity

print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(8, [5, 2, 3]))
print(how_sum(7, [2, 4, 6]))
print(how_sum(0, [1, 2, 4, 6]))

print(how_sumo(7, [5, 3, 4, 7]))
print(how_sumo(8, [5, 2, 3]))
print(how_sumo(9, [2, 4, 6]))
print(how_sumo(0, [1, 2, 4, 6]))
print(how_sumo(300, [7, 14]))