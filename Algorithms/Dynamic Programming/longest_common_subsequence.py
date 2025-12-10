# Leetcode 1143. Longest Common Subsequence

# https://leetcode.com/problems/longest-common-subsequence/description/

# 2D Dynamic Programming (DP) method
def lcs_length(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    print(dp)
    return dp[0][0]

# O(m * n) - Time complexity
# O(m * n) (can be reduced to O(min(m, n))) - Space complexity

# 2D DP with space optimized to O(min(m, n))
def lcs_length_optimized(a: str, b: str) -> int:
    # Always make b the shorter string to minimize space
    if len(a) < len(b):
        a, b = b, a
    n = len(b)
    next_row = [0]*(n + 1)
    for i in range(len(a) - 1, -1, -1):
        curr = [0]*(n + 1)
        for j in range(n - 1, -1, -1):
            if a[i] == b[j]:
                curr[j] = 1 + next_row[j + 1]
            else:
                curr[j] = max(next_row[j], curr[j + 1])
        next_row = curr
    return next_row[0]

# O(m * n) - Time complexity
# O(min(m, n)) - Space complexity


# Reconstruct the Longest Common Subsequence (LCS) string
def lcs_string(text1: str, text2: str) -> str:
    m, n = len(text1), len(text2)
    dp = [[0]*(n + 1) for _ in range(m+1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    # Backtrack to build the sequence
    i = j = 0
    out = []
    while i < m and j < n:
        if text1[i] == text2[j]:
            out.append(text1[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return ''.join(out)

# O(m * n) - Time complexity
# O(m * n) (can be reduced to O(min(m, n))) - Space complexity

print(lcs_length('abcde', 'ace')) # 3
print(lcs_length('abc', 'abc')) # 3
print(lcs_length('abc', 'def')) # 0

print(lcs_length_optimized('abcde', 'ace')) # 3
print(lcs_length_optimized('abc', 'abc')) # 3
print(lcs_length_optimized('abc', 'def')) # 0

print(lcs_string('abcde', 'ace')) # 'ace'
print(lcs_string('abc', 'abc')) # 'abc'
print(lcs_string('abc', 'def')) # ''