# Leetcode 39. Combination Sum

# https://leetcode.com/problems/combination-sum/description/

# Backtracking

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    path = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            num = candidates[i]

            # choose
            path.append(num)

            # stay at i because we can reuse the same number
            backtrack(i, remaining - num)

            # undo choice
            path.pop()

    backtrack(0, target)
    return result


# Slightly Optimzied solution
def combination_sum_o(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    result = []
    path = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            num = candidates[i]

            if num > remaining:
                break

            path.append(num)
            backtrack(i, remaining - num)
            path.pop()

    backtrack(0, target)
    return result
