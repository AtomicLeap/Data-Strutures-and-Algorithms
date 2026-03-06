# Leetcode 5. Longest Palindromic Substring

# https://leetcode.com/problems/longest-palindromic-substring/description/

# Tags -> Two Pointers, String, Dynamic Programming

def longest_palindrome(s: str) -> str:
    n = len(s)
    if n < 2:
        return s

    start = 0
    max_len = 1

    def expand(left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # return starting index and length
        return left + 1, right - left - 1

    for i in range(n):
        # Odd-length palindrome
        l1, len1 = expand(i, i)

        # Even-length palindrome
        l2, len2 = expand(i, i + 1)

        if len1 > max_len:
            start = l1
            max_len = len1

        if len2 > max_len:
            start = l2
            max_len = len2

    return s[start:start + max_len]

# n = len(s)
# O(n ^ 2) Time complexity
# O(1) Space complexity 

print(longest_palindrome("babad")) # "bab"
print(longest_palindrome("cbbd")) # "bb"
