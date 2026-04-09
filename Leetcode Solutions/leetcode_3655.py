# Leetcode 3655. XOR After Range Multiplication Queries II

# https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/description

# Tags -> Divide and Conquer, Array

from collections import defaultdict
from math import sqrt

def xor_after_queries(nums: list[int], queries: list[list[int]]) -> int:
    MOD = 10**9 + 7
    n = len(nums)
    sq = int(sqrt(n))
    mp = defaultdict(list)

    for l, r, k, v in queries:
        if k > sq:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % MOD
        else:
            mp[k].append((l, r, v))

    for k in mp:
        dif = [1] * (n + k)
        for l, r, v in mp[k]:
            dif[l] = (dif[l] * v) % MOD
            rplus1 = l + ((r - l) // k + 1) * k  # l + items * size of each step
            dif[rplus1] = (dif[rplus1] * pow(v, -1, MOD)) % MOD

        for i in range(k, n):
            dif[i] = (dif[i] * dif[i - k]) % MOD

        for i in range(n):
            nums[i] = (dif[i] * nums[i]) % MOD

    result = 0
    for x in nums:
        result ^= x

    return result

# O(q * sqrt(n) + n * sqrt(n)) - Time complexity
# O(n) - Space complexity

print(xor_after_queries([1, 2, 3, 4], [[0, 3, 2, 2], [0, 3, 1, 2]])) # 0
print(xor_after_queries([1, 2, 3, 4], [[0, 3, 2, 2], [0, 3, 1, 2], [0, 3, 1, 2]])) # 2

