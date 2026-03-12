# Leetcode 3130. Find All Possible Stable Binary Arrays II

# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/description/

# Tags -> Dynamic Programming, Prefix Sum

def number_of_Stable_arrays(zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        table = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        
        for i in range(1, min(limit, zero) + 1):
            table[i][0][0] = 1
        for j in range(1, min(limit, one) + 1):
            table[0][j][1] = 1
        
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                x = 0 if i - limit - 1 < 0 else table[i - limit - 1][j][1]
                y = 0 if j - limit - 1 < 0 else table[i][j - limit - 1][0]
                table[i][j][0] = (table[i - 1][j][0] + table[i - 1][j][1] - x) % MOD
                table[i][j][1] = (table[i][j - 1][0] + table[i][j - 1][1] - y) % MOD
        return sum(table[zero][one]) % MOD


# O(zero * one) - Time complexity
# O(zero * one) - Space complexity

print(number_of_Stable_arrays(1, 1, 2)) # 2
print(number_of_Stable_arrays(1, 2, 1)) # 1
print(number_of_Stable_arrays(3, 3, 2)) # 14