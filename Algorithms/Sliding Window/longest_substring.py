# Leetcode 3. Longest Substring Without Repeating Characters

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

def longest_sub_string(s: str) -> int:
    total, left, visited = 0, 0, {}

    for right, char in enumerate(s):
        if char in visited and visited[char] >= left:
            left = visited[char] + 1
        visited[char] = right
        total = max(total, right - left + 1)
    return total

# O(n) Time complexity
# O(n) Space complexity

print(longest_sub_string('abcabcbb')) # 3
print(longest_sub_string('abcabcbdhkmvebhgkldgg')) # 9
print(longest_sub_string('abcdefabctyuimnbcbb')) # 12
print(longest_sub_string('abcdefghijkl')) # 12
print(longest_sub_string('aaaaaaaaaaaaaa')) # 1

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