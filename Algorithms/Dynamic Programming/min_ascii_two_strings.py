# Leetcode 712. Minimum ASCII Delete Sum for Two Strings

# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/

# Key idea
"""
Let table[i][j] = minimum ASCII delete sum to make s1[i:] and s2[j:] equal.

Transitions:
1. If s1[i] == s2[j]: keep both → table[i][j] = table[i+1][j+1]
2. Else: you must delete one char:
    - delete s1[i] → ord(s1[i]) + table[i+1][j]
    - delete s2[j] → ord(s2[j]) + table[i][j+1]
3. take min of those two

Base cases:
table[n][j] = sum of ASCII codes of s2[j:] (must delete all remaining chars in s2)
table[i][m] = sum of ASCII codes of s1[i:]
Because lengths are up to 1000, use a 1D DP (space optimized).
"""

# Use 2 D table - Tabulation
def minimum_delete_sum(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    table = [[0]*(m + 1) for _ in range(n + 1)]

    for i in range(m - 1,-1,-1):
        table[-1][i] = table[-1][i + 1] + ord(s2[i])

    for i in range(n - 1,-1,-1):
        table[i][-1] = table[i + 1][-1] + ord(s1[i])

    for i in range(n - 1,-1,-1):
        for j in range(m - 1,-1,-1):

            if s1[i] == s2[j]:
                table[i][j] = table[i+1][j+1]
            else:
                table[i][j] = min(ord(s1[i]) + table[i + 1][j], ord(s2[j]) + table[i][j+1]) 
    return table[0][0]

# Let n, m = len(s1), len(s2)
# O(m . n) - Time complexity
# O(m . n) - Space complexity

# Use 1 D table - Tabulation
def min_ascii_sum(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)

    # table[j] will represent table[i][j] for current i, iterating i from n down to 0
    table = [0] * (m + 1)

    # Base: table[n][j] = sum(ord(s2[j:]))
    for j in range(m - 1, -1, -1):
        table[j] = table[j + 1] + ord(s2[j])

    # Fill from i = n-1 down to 0
    for i in range(n - 1, -1, -1):
        prev_diag = table[m]          # table[i+1][m] from previous row
        table[m] = table[m] + ord(s1[i]) # table[i][m] = table[i+1][m] + ord(s1[i])

        for j in range(m - 1, -1, -1):
            temp = table[j]  # table[i+1][j] before overwrite

            if s1[i] == s2[j]:
                table[j] = prev_diag  # table[i][j] = table[i+1][j+1]
            else:
                # delete_s1 = ord(s1[i]) + table[j]      # table[i+1][j] is temp (but table[j] currently is table[i+1][j] before update? we saved in temp)
                delete_s1 = ord(s1[i]) + temp
                delete_s2 = ord(s2[j]) + table[j + 1]  # table[i][j+1] already updated in this row
                table[j] = min(delete_s1, delete_s2)

            prev_diag = temp  # move diagonal for next j (table[i+1][j])

    return table[0]

# Let n, m = len(s1), len(s2)
# O(m . n) - Time complexity
# O(m) - Space complexit

print(minimum_delete_sum(s1 = "sea", s2 = "eat")) # 231
print(minimum_delete_sum("delete", s2 = "leet")) # 403
print(min_ascii_sum(s1 = "sea", s2 = "eat")) # 231
print(min_ascii_sum("delete", s2 = "leet")) # 403