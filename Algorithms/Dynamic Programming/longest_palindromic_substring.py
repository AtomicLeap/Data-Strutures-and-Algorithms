# Leetcode 5. Longest Palindromic Substring

# https://leetcode.com/problems/longest-palindromic-substring/description/


def longest_palindrome(s: str) -> str:
    if len(s) < 2 or s == s[::-1]:
        return s  # quick outs for short and already-palindromic strings

    start, best = 0, 1  # best substring is s[start:start+best]

    def expand(l: int, r: int) -> None:
        nonlocal start, best
        # expand while in bounds and matching
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # when loop breaks, palindrome is s[l+1:r]
        if r - (l + 1) > best:
            start, best = l + 1, r - (l + 1)

    for i in range(len(s) - 1):
        # odd-length center at i
        expand(i, i)
        # even-length center between i and i+1
        expand(i, i + 1)

    return s[start:start + best]

# O(n ^ 2) Time complexity
# O(1) Space complexity

print(longest_palindrome("babad"))  # "bab" (or "aba")
print(longest_palindrome("cbbd"))   # "bb"
print(longest_palindrome("a"))      # "a"
print(longest_palindrome("ac"))     # "a" or "c"
