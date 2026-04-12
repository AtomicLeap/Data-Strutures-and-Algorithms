# Leetcode 3791. Number of Balanced Integers in a Range

# https://leetcode.com/problems/number-of-balanced-integers-in-a-range/description/

# Tags -> Math, String, hard

from functools import lru_cache


def count_balanced_numbers(low: int, high: int) -> int:
    def count_upto(x: int) -> int:
        if x < 10:
            return 0  # balanced numbers need at least 2 digits

        s = str(x)
        n = len(s)

        def count_with_length(L: int) -> int:
            # Count balanced L-digit numbers <= x
            # If L < n: upper bound is 99...9
            # If L == n: upper bound is s itself
            if L < 2:
                return 0

            limit = s if L == n else "9" * L

            @lru_cache(None)
            def dfs(pos: int, diff: int, tight: bool) -> int:
                if pos == L:
                    return 1 if diff == 0 else 0

                up = int(limit[pos]) if tight else 9
                total = 0

                for d in range(up + 1):
                    # no leading zero
                    if pos == 0 and d == 0:
                        continue

                    # positions are 1-indexed from the left
                    position = pos + 1
                    if position % 2 == 1:   # odd position
                        new_diff = diff + d
                    else:                   # even position
                        new_diff = diff - d

                    total += dfs(pos + 1, new_diff, tight and d == up)

                return total

            return dfs(0, 0, True)

        ans = 0
        for L in range(2, n + 1):
            ans += count_with_length(L)
        return ans

    return count_upto(high) - count_upto(low - 1)

# O(log(high)) Time complexity - We count balanced numbers by digit length, and for each length, we use a DFS with memoization that explores at most 10^L states, but since L is at most log10(high), this is manageable.
# O(L * 10^L) Space complexity - The memoization cache can store results

print(count_balanced_numbers(1, 100)) # 9
print(count_balanced_numbers(1, 1000)) # 108
print(count_balanced_numbers(1, 10000)) # 1080
print(count_balanced_numbers(120, 129)) # 1
print(count_balanced_numbers(1234, 1234)) # 0

