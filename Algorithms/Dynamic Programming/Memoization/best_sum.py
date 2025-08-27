# best sum problem

"""
Write a function "best_sum(target, nums)" that takes a target 
and an array of numbers as arguements. The function should 
return an array containing the shortest combination of numbers that
add up to exactly the target. If there is no combination that 
adds up to the target, then return None.

Constraints
If there is a tie for the shortest combination, you may return any of 
the shortest. You may assume that all input numbers are non-negative.
"""

# Brute force solution
def best_sum(target: int, numbers: list[int]) -> list[int] | None:
    if target == 0:
        return []
    if target < 0:
        return None

    best_combination = None
    
    for num in numbers:
        remainder = target - num
        results = best_sum(remainder, numbers)
        if results != None:
            combination = results + [num]
            if not best_combination or best_combination and len(combination) < len(best_combination):
                best_combination = combination
    return best_combination
# m = size of target
# n = len(numbers)
# O(n^m) Time complexity
# O(m ^2) Space complexity => max stack depth of m * size of retuned array m

# Optimized solution
def best_sumo(target: int, numbers: list[int], memo: dict = {}) -> list[int] | None:
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    best_combination = None
    
    for num in numbers:
        remainder = target - num
        results = best_sumo(remainder, numbers, memo)
        if results != None:
            combination = results + [num]
            if not best_combination or best_combination and len(combination) < len(best_combination):
                best_combination = combination
    memo[target] = best_combination
    return best_combination
# m = size of target
# n = len(numbers)
# O(m * n) Time complexity
# O(m * m) Space complexity
    


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))

print(best_sumo(100, [1, 2, 7, 5, 25]))