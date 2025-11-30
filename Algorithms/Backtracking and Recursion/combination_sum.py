# Leetcode 39. Combination Sum

# https://leetcode.com/problems/combination-sum/description/

# Dynamic Programming method (Tabulation)

def combination_sum_i(candidates: list[int], target: int) -> list[list[list[int]]] | list:
    candidates.sort() # Optional but useful for pruning

    table = [[] for _ in range(target + 1)]
    table[0] = [[]] # one way to make 0: take nothing

    for i in range(target + 1):
        if table[i]:
            for candidate in candidates:
                if i + candidate > target:
                    break

                for combination in table[i]:
                    # Enforce non-decreasing order to avoid permutations:
                    # only allow adding 'candidate' if it's >= last element in combination
                    if combination and candidate < combination[-1]:
                        continue

                    combination = combination + [candidate]
                    table[i + candidate].append(combination)
    return table[target]


# Backtracking Method
from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[List[int]]] | list:
    candidates.sort()          # Optional but useful for pruning
    result = []

    def backtrack(start: int, remaining: int, path: List[int]) -> None:
        # If we hit the target exactly, record the combination
        if remaining == 0:
            result.append(path.copy())
            return

        # If we overshoot, stop exploring this path
        if remaining < 0:
            return

        # Try all candidates starting from 'start'
        for i in range(start, len(candidates)):
            val = candidates[i]

            # Prune: no need to continue if current number already > remaining
            if val > remaining:
                break

            # Choose the current candidate
            path.append(val)
            # Because we can reuse the same candidate, we call backtrack with 'i' (not i+1)
            backtrack(i, remaining - val, path)
            # Backtrack: undo the choice
            path.pop()

    backtrack(0, target, [])
    return result

# O (S) - Time complexity - Where S is the total number of nodes explored in the recursion tree.
# O (K . L) - Space complexity - where: K = number of valid combinations, L = average length of each combination


print(combination_sum([2,3,6,7], 7)) # [[2,2,3],[7]]
print(combination_sum([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(combination_sum([2], 1)) # []

print(combination_sum_i([2,3,6,7], 7)) # [[2,2,3],[7]]
print(combination_sum_i([2,3,5], 8)) # [[2,2,2,2],[2,3,3],[3,5]]
print(combination_sum_i([2], 1)) # []