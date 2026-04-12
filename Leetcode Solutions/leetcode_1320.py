# Leetcode 1320. Minimum Distance to Type a Word Using Two Fingers

# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/

# Tags -> Dynamic Programming, Memoization, String, hard

from math import inf


def minimum_distance(word: str) -> int:
    UNUSED = 26

    def dist(a: int, b: int) -> int:
        if a == UNUSED or b == UNUSED:
            return 0
        ax, ay = divmod(a, 6)
        bx, by = divmod(b, 6)
        return abs(ax - bx) + abs(ay - by)

    # dp[f1][f2] = minimum cost after typing processed prefix
    dp = [[inf] * 27 for _ in range(27)]
    dp[UNUSED][UNUSED] = 0

    for ch in word:
        c = ord(ch) - ord('A')
        new_dp = [[inf] * 27 for _ in range(27)]

        for f1 in range(27):
            for f2 in range(27):
                if dp[f1][f2] == inf:
                    continue

                cur = dp[f1][f2]

                # Use finger 1 to type c
                new_dp[c][f2] = min(new_dp[c][f2], cur + dist(f1, c))

                # Use finger 2 to type c
                new_dp[f1][c] = min(new_dp[f1][c], cur + dist(f2, c))

        dp = new_dp

    result = inf
    for i in range(27):
        for j in range(27):
            result = min(result, dp[i][j])

    return int(result)

# O(n) Time complexity - we process each character in the word and for each character, we iterate through the dp array which has a fixed size of 27x27
# O(1) Space complexity - the dp array has a fixed size of 27x27

print(minimum_distance("CAKE")) # 3
print(minimum_distance("HAPPY")) # 6
print(minimum_distance("NEW")) # 3
print(minimum_distance("YEAR")) # 7

