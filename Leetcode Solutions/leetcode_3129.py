# Leetcode 3129. Find All Possible Stable Binary Arrays I

# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/description

# Tags -> Dynamic Programming, Prefix Sum

def number_of_Stable_arrays(zero: int, one: int, limit: int) -> int:
    MOD = 10**9 + 7

    zero_table = [[0] * (one + 1) for _ in range(zero + 1)]
    one_table = [[0] * (one + 1) for _ in range(zero + 1)]

    # Base cases: arrays made of only 0s
    for i in range(1, min(zero, limit) + 1):
        zero_table[i][0] = 1

    # Base cases: arrays made of only 1s
    for j in range(1, min(one, limit) + 1):
        one_table[0][j] = 1

    for i in range(1, zero + 1):
        for j in range(1, one + 1):
            # Arrays ending with 0
            zero_table[i][j] = (zero_table[i - 1][j] + one_table[i - 1][j]) % MOD
            if i - limit - 1 >= 0:
                zero_table[i][j] = (zero_table[i][j] - one_table[i - limit - 1][j]) % MOD

            # Arrays ending with 1
            one_table[i][j] = (zero_table[i][j - 1] + one_table[i][j - 1]) % MOD
            if j - limit - 1 >= 0:
                one_table[i][j] = (one_table[i][j] - zero_table[i][j - limit - 1]) % MOD

    return (zero_table[zero][one] + one_table[zero][one]) % MOD

# O(zero * one) - Time complexity
# O(zero * one) - Space complexity

print(number_of_Stable_arrays(1, 1, 2)) # 2
print(number_of_Stable_arrays(1, 2, 1)) # 1
print(number_of_Stable_arrays(3, 3, 2)) # 14
