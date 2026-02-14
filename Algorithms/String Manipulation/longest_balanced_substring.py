# Leetcode 3713. Longest Balanced Substring I

# https://leetcode.com/problems/longest-balanced-substring-i/description

def longest_balanced(s: str) -> int:
    n = len(s)
    longest_substring = 0

    for left in range(n):
        freq_array = [0] * 26
        for right in range(left, n):
            idx = ord(s[right]) - ord('a')
            freq_array[idx] += 1
        min_val = n
        max_val = 0
        for num in freq_array:
            if num and num > max_val:
                max_val = num
            if num and num < min_val:
                min_val = num
        if min_val == max_val:
            substring_length = right - left + 1
            longest_substring = max(longest_substring, substring_length)
    return longest_substring


def longest_balanced_i(s: str) -> int:
    n = len(s)
    result = 1  # any single character is balanced

    for i in range(n):
        freq_array = [0] * 26
        for j in range(i, n):
            idx = ord(s[j]) - 97
            freq_array[idx] += 1

            min_freq = 10**9
            max_freq = 0
            for freq in freq_array:
                if freq:
                    if freq < min_freq: min_freq = freq
                    if freq > max_freq: max_freq = freq

            if min_freq == max_freq:  # all present characters appear the same number of times
                result = max(result, j - i + 1)

    return result
    



