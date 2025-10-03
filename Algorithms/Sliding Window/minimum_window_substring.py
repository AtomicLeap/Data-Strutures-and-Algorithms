# Leetcode 76. Minimum Window Substring

"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring 
of s such that every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

from collections import Counter

def min_window_substring(s: str, t: str) -> str:
    if len(t) > len(s): 
        return ""

    need = Counter(t)                 # counts required for each char in t
    have = 0                          # number of chars whose counts are satisfied
    need_kinds = len(need)

    window = {}                       # current window counts
    res = (float('inf'), None, None)  # (length, left, right)
    left = 0

    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            have += 1

        # When window satisfies all requirements, try to shrink it
        while have == need_kinds:
            if (right - left + 1) < res[0]:
                res = (right - left + 1, left, right)

            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                have -= 1
            left += 1

    _, left, right = res
    return "" if left is None else s[left:right+1]

# O(m + n) Time complexity
# O(k) ≈ O(1) Space complexity --> for English alphabet

print(min_window_substring("ADOBECODEBANC", "ABC")) # "BANC"
print(min_window_substring("a", "a")) # "a"
print(min_window_substring("a", "aa")) # ""