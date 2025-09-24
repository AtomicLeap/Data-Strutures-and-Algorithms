# Leetcode 3. Longest Substring Without Repeating Characters

"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

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