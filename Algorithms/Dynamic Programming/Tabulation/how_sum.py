# can sum problem

# Write a function "how_sum(target, nums)" that takes a target 
# and an array of numbers as arguements. The function should 
# return an array containing any combination of elements that
# add up to exactly the target. If there is no combination that 
# adds up to the target, then return None.

# Constraints
# If there are multiple combinations possible, you may return any 
# single one. You may assume that all input numbers are non-negative.

# Tabulation solution
def how_sum(target: int, numbers: list[int]) -> list[int] | None:
    table = [None for _ in range(target + 1)]
    table[0] = [] # base case - we need no element to generate a target sum of zero

    for i in range(target + 1):
        if table[i] != None:
            for num in numbers:
                if i  + num < target + 1:
                    table[i + num] = table[i] + [num]
    return table[target]

# m = size of target
# n = len(nums)
# O(n * m) Time complexity
# O(m * m) Space complexity => size of the table and created array


print(how_sum(7, [5, 3, 4, 7])) # [4, 3]
print(how_sum(8, [5, 2, 3])) # [2, 2, 2, 2]
print(how_sum(9, [2, 4, 6])) # None
print(how_sum(0, [1, 2, 4, 6])) # []
print(how_sum(300, [7, 14])) # None