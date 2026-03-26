# Leetcode 1866. Number of Ways to Rearrange Sticks With K Sticks Visible

# https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/description/

# Tags -> Dynamic Programming

def rearrange_sticks(n: int, k: int) -> int:
    MOD = 10**9 + 7
    table = [[0] * (k + 1) for _ in range(n + 1)]
    
    table[0][0] = 1
    
    for r in range(1, n + 1):
        for c in range(1, min(r, k) + 1):
            table[r][c] = (table[r - 1][c - 1] + (r - 1) * table[r - 1][c]) % MOD
    
    return table[n][k]

print(rearrange_sticks(3, 2)) # 3
print(rearrange_sticks(5, 5)) # 1  
print(rearrange_sticks(20, 11)) # 647427950

# O (n * k) - Time complexity
# O (n * k) - Space complexity

def rearrange_sticks_i(n: int, k: int) -> int:
    MOD = 10**9 + 7
    
    # table[c] = number of ways for current r sticks to have exactly c visible
    table = [0] * (k + 1)
    table[1] = 1  # for n = 1
    
    for r in range(2, n + 1):
        # update backwards so table[c-1] is still from previous row
        upper = min(r, k)
        for c in range(upper, 0, -1):
            table[c] = (table[c - 1] + (r - 1) * table[c]) % MOD
    
    return table[k]

# O (n * k) - Time complexity
# O (k) - Space complexity

print(rearrange_sticks_i(3, 2)) # 3
print(rearrange_sticks_i(5, 5)) # 1
print(rearrange_sticks_i(20, 11)) # 647427950
