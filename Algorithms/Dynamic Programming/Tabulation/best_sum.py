# best sum problem --> It implements the Greedy Algorithm

# Write a function "best_sum(target, nums)" that takes a target 
# and an array of numbers as arguements. The function should 
# return an array containing the shortest combination of numbers that
# add up to exactly the target. If there is no combination that 
# adds up to the target, then return None.

# Constraints
# If there is a tie for the shortest combination, you may return any of 
# the shortest. You may assume that all input numbers are non-negative.

# Tabulation solution
def best_sum(target: int, numbers: list[int]) -> list[int] | None:
    table = [None for _ in range(target + 1)]
    table[0] = []

    for i in range(target + 1):
        if table[i] != None:
            for num in numbers:
                if i + num < target + 1:
                    combination = table[i] + [num]
                    if not table[i + num] or len(combination) < len(table[i + num]):
                        table[i + num] = combination
    return table[target]

# m = size of target
# n = len(numbers)
# O(n * m * m) Time complexity
# O(m * m) Space complexity => size of the table and created array
    


print(best_sum(7, [5, 3, 4, 7])) # 7
print(best_sum(8, [2, 3, 5])) # [3, 5]
print(best_sum(8, [1, 4, 5])) # [4, 4]
print(best_sum(100, [1, 2, 7, 5, 25])) # [25, 25, 25, 25]