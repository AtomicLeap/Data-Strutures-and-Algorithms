# Leetcode 1680. Concatenation of Consecutive Binary Numbers

# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description

# Tags -> Math, Bit Manipulation, Simulation

def concatenate_binary(n: int) -> int:
    MOD = 10**9 + 7
    result = 0
    bit_len = 0

    for i in range(1, n + 1):
        # if i is a power of two, its bit-length increases by 1
        if (i & (i - 1)) == 0:
            bit_len += 1

        result = ((result << bit_len) + i) % MOD

    return result

# O(n) - Time complexity
# O(1) - Space complexity

print(concatenate_binary(1)) # 1
print(concatenate_binary(3)) # 27
print(concatenate_binary(12)) # 505379714
