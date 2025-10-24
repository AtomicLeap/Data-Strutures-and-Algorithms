# 647. Palindromic Substrings

# https://leetcode.com/problems/palindromic-substrings/description/

def palindromic_substrings(s: str) -> int:
    n = len(s)
    ans = 0
    # There are 2n - 1 centers: indices 0..n-1 for odd, and "between" positions for even
    for c in range(2 * n - 1):
        left = c // 2
        right = left + (c % 2)  # same for odd; next char for even
        # expand while s[left..right] is a palindrome
        while left >= 0 and right < n and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1
    return ans

# O(n ^ 2) Time complexity
# O(1) Space complexity

print(palindromic_substrings("abc")) # "a", "b", "c".
print(palindromic_substrings("aaa")) # "a", "a", "a", "aa", "aa", "aaa".