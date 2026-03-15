# Leetcode 39. Combination Sum

# https://leetcode.com/problems/combination-sum/description/

# Backtracking

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    combination = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(combination[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            num = candidates[i]

            # choose
            combination.append(num)

            # stay at i because we can reuse the same number
            backtrack(i, remaining - num)

            # undo choice
            combination.pop()

    backtrack(0, target)
    return result

# O(n ^ 2) - Worst case, O(number of valid states explored) - Time complexity
# O(target) - Space complexity

# Slightly Optimzied solution
def combination_sum_o(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []
    combination = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(combination.copy())
            return

        for i in range(start, len(candidates)):
            num = candidates[i]

            if num > remaining:
                break

            combination.append(num)
            backtrack(i, remaining - num)
            combination.pop()

    backtrack(0, target)
    return result

# O(n ^ 2) - Worst case, O(number of valid states explored) - Time complexity
# O(target) - Space complexity