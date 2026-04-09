# Leetcode 3653. XOR After Range Multiplication Queries I

# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description

# Tags -> Divide and Conquer, Array, Simulation

def xor_after_queries(nums: list[int], queries: list[list[int]]) -> int:
    MOD = 10**9 + 7

    for l, r, k, v in queries:
        idx = l
        while idx <= r:
            nums[idx] = (nums[idx] * v) % MOD
            idx += k

    result = 0
    for num in nums:
        result ^= num

    return result

# O(q * n) - Time complexity
# O(1) - Space complexity

print(xor_after_queries([1, 2, 3, 4], [[0, 3, 2, 2], [0, 3, 1, 2]])) # 0
print(xor_after_queries([1, 2, 3, 4], [[0, 3, 2, 2], [0, 3, 1, 2], [0, 3, 1, 2]])) # 2

