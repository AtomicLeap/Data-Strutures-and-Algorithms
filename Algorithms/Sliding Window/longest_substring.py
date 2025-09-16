# Leetcode 3. Longest Substring Without Repeating Characters

"""
Given a string s, find the longest substring without repeating characters.
Write a function `longest_substring` that takes a string s, and returns 
the longest sub-string.

Input: 'abcabcbb'
Output: abc
"""
def longest_substring(s: str) -> str:
    n = len(s)
    final_substring = ''

    for i in range(n):
        substring = ''
        visited = {}

        while i < n and s[i] not in visited:
            visited[s[i]] = 1
            substring += s[i]
            i += 1
        if len(substring) > len(final_substring):
            final_substring = substring
    return final_substring

# O(n) Time complexity
# O(n) Space complexity

print(longest_substring('abcabcbb')) # 'abc'
print(longest_substring('abcabcbdhkmvebhgkldgg')) # 'mvebhgkld'
print(longest_substring('abcdefabctyuimnbcbb')) # 'defabctyuimn'
print(longest_substring('abcdefghijkl')) # 'abcdefghijkl'
print(longest_substring('aaaaaaaaaaaaaa')) # 'a'