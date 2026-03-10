# Leetcode 76. Minimum Window Substring

# https://leetcode.com/problems/minimum-window-substring/description/

# Tags -> String, Sliding Window, Two-Pointer, Hash Table

from collections import Counter

def min_window(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    required_chars = Counter(t)
    unique_chars_count = len(required_chars)
    window = {}
    results = (float("inf"), 0, 0)
    satisfied_chars_count = 0
    left = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1
        if char in required_chars and window[char] == required_chars[char]:
            satisfied_chars_count += 1
        
        # shrink from left
        while satisfied_chars_count == unique_chars_count:
            if (right - left + 1) < results[0]:
                results = (right - left + 1, left, right)
            
            left_char = s[left]
            window[left_char] -= 1
            if left_char in required_chars and window[left_char] < required_chars[left_char]:
                satisfied_chars_count -= 1
            
            left += 1
        
    min_len, left, right = results
    return "" if min_len == float("inf") else s[left:right + 1]

# Len m, n, k = len(s), len(t), 26 (number of alphabets)
# O(m + n) Time complexity
# O(k) ≈ O(1) Space complexity --> for English alphabet

print(min_window("ADOBECODEBANC", "ABC")) # "BANC"
print(min_window("a", "a")) # "a"
print(min_window("a", "aa")) # ""
