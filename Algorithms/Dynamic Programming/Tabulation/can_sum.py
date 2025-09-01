# can sum problem

# Write a function "can_sum(target, nums)" that takes a target 
# and an array of numbers as arguements. The function should 
# return a boolean indicating whether or not it is possible 
# to generate the target sum using numbers from the array.

# Constraints
# You may use an element of the array as many times as needed.
# You may assume that all input numbers are non-negative.

# Tabulation solution
def can_sum(target: int, nums: list[int]) -> bool:
    table = [False for _ in range(target + 1)]
    table[0] = True

    for i in range(target + 1):
        if table[i] ==  True:
            for num in nums:
                if i + num < target + 1:
                    table[i + num] = True
    return table[target]

# m = size of target
# n = len(nums)
# O(n * m) Time complexity
# O(m) Space complexity => size of the table


print(can_sum(7, [2, 4])) # False
print(can_sum(23, [2, 7, 4, 5])) # True
print(can_sum(18, [2, 3, 4, 5])) # True
print(can_sum(30, [7, 11, 14])) # False
print(can_sum(301, [11])) # False
print(can_sum(93, [7, 9, 5, 14])) # True
