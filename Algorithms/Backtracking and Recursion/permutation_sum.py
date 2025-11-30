# Permutation Sum

"""
For below combination sum problem, this is a Dynamic Programming solution 
that provides permutation results. This is an adaptation to show permutation.
"""

# https://leetcode.com/problems/combination-sum/description/

# Iteratively (Tabulation)
def permutation_sum(candidates: list[int], target: int) -> list[list[int]] | list:
    table = [[] for _ in range(target + 1)]
    table[0] = [[]] # one way to make 0: take nothing

    for i in range(target + 1):
        if table[i]:
            for candidate in candidates:
                if i + candidate <= target:
                    permutation = [[*item, candidate] for item in table[i]]
                    table[i + candidate] += permutation
    return table[target]

# m = size of target
# n = len(numbers)
# O(n ^ m) Time complexity => Exponential time
# O(n * m) Space complexity => Exponential space

print(permutation_sum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(permutation_sum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(permutation_sum([2], 1)) # []