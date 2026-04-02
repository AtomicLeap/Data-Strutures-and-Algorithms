# Leetcode 3418. Maximum Amount of Money Robot Can Earn

# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/description

# Tags -> Array, Dynamic Programming, Matrix, Simulation

from typing import List

def maximum_amount(coins: List[List[int]]) -> int:
    m, n = len(coins), len(coins[0])
    NEG_INF = float('-inf')

    # prev[j][k] = best answer for previous row at column j using k neutralizations
    prev = [[NEG_INF] * 3 for _ in range(n)]

    for i in range(m):
        curr = [[NEG_INF] * 3 for _ in range(n)]

        for j in range(n):
            val = coins[i][j]

            for used in range(3):
                best_same_used = NEG_INF
                best_prev_used = NEG_INF

                # from top
                if i > 0:
                    best_same_used = max(best_same_used, prev[j][used])
                    if used > 0:
                        best_prev_used = max(best_prev_used, prev[j][used - 1])

                # from left
                if j > 0:
                    best_same_used = max(best_same_used, curr[j - 1][used])
                    if used > 0:
                        best_prev_used = max(best_prev_used, curr[j - 1][used - 1])

                # starting cell
                if i == 0 and j == 0:
                    if val >= 0:
                        curr[j][0] = val
                    else:
                        # either do not neutralize or neutralize at the start
                        curr[j][0] = val
                        curr[j][1] = 0
                    continue

                if val >= 0:
                    if best_same_used != NEG_INF:
                        curr[j][used] = best_same_used + val
                else:
                    # Option 1: take the loss
                    if best_same_used != NEG_INF:
                        curr[j][used] = max(curr[j][used], best_same_used + val)

                    # Option 2: neutralize this robber
                    if used > 0 and best_prev_used != NEG_INF:
                        curr[j][used] = max(curr[j][used], best_prev_used)

        prev = curr

    return max(prev[n - 1])
    
# O(m * n) Time complexity
# O(n) Space complexity since we only keep the previous row

print(maximum_amount([[0,1,-1],[1,-2,3],[2,-3,4]])) # 8
print(maximum_amount([[10,10,10],[10,10,10]])) # 40