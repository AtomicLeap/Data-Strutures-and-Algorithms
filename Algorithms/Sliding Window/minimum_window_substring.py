# Leetcode 76. Minimum Window Substring

# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

def min_window_substring(s: str, t: str) -> str:
    if len(t) > len(s): 
        return ""

    required_char_count = Counter(t)  # counts required for each char in t
    required_chars_statisfied = 0     # number of chars whose counts are satisfied
    required_chars_kinds = len(required_char_count)

    window = {}                       # current window counts
    results = (float('inf'), None, None)  # (length, left, right)
    left = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1
        if char in required_char_count and window[char] == required_char_count[char]:
            required_chars_statisfied += 1

        # When window satisfies all requirements, try to shrink it
        while required_chars_statisfied == required_chars_kinds:
            if (right - left + 1) < results[0]:
                results = (right - left + 1, left, right)

            left_char = s[left]
            window[left_char] -= 1
            if left_char in required_char_count and window[left_char] < required_char_count[left_char]:
                required_chars_statisfied -= 1
            left += 1

    _, left, right = results
    return "" if left is None else s[left:right+1]

# O(m + n) Time complexity
# O(k) ≈ O(1) Space complexity --> for English alphabet

print(min_window_substring("ADOBECODEBANC", "ABC")) # "BANC"
print(min_window_substring("a", "a")) # "a"
print(min_window_substring("a", "aa")) # ""