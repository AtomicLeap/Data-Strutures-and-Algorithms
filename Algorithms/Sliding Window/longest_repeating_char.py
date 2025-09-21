# Leetcode 424. Longest Repeating Character Replacement

"""
You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation 
at most k times.
Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 
Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

def character_replacement(s: str, k: int) -> int:
    counts = [0] * 26
    l = 0
    max_freq = 0
    best = 0

    for r, ch in enumerate(s):
        idx = ord(ch) - ord('A')
        counts[idx] += 1
        max_freq = max(max_freq, counts[idx])

        # If we need more than k changes to unify this window, shrink it
        while (r - l + 1) - max_freq > k:
            counts[ord(s[l]) - ord('A')] -= 1
            l += 1

        best = max(best, r - l + 1)

    return best

# n = len(s)
# O(n) - Time complexity
# O(1) - Space complexity -> fixed 26-size frequency array

print(character_replacement("ABAB", 2)) # 4
print(character_replacement("AABABBA", 1)) # 4