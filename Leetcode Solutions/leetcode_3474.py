# Leetcode 3474. Lexicographically Smallest Generated String

# https://leetcode.com/problems/lexicographically-smallest-generated-string/description

# Tags -> String, Greedy, hard

# Idea
"""
To generate the lexicographically smallest string, we can iterate through the input string and for each character, we can replace it with the smallest character that is greater than or equal to it. We can use a list to store the characters of the input string and then join them together at the end to get the final result.
"""

def generate_string(str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)
    result = ['a'] * (m + n - 1)
    used = [False] * (m + n - 1)

    for i in range(m):
        if str1[i] == 'T':
            for j in range(i, i + n):
                if used[j] and result[j] != str2[j - i]:
                    return ""
                result[j] = str2[j - i]
                used[j] = True

    for i in range(m):
        if str1[i] == 'F':
            if all(result[j] == str2[j - i] for j in range(i, i + n)):
                mismatch = False
                for j in range(i + n - 1, i - 1, -1):
                    if not used[j]:
                        result[j] = 'b'
                        mismatch = True
                        break
                if not mismatch:
                    return ""

    return "".join(result)


# O(m*n) Time complexity
# O(m+n) Space complexity

print(generate_string("TFTF", "ab")) # "ababa"
print(generate_string("TFTF", "abc")) # ""
print(generate_string("F", "d")) # "a"
