# Leetcode 424. Longest Repeating Character Replacement

# https://leetcode.com/problems/longest-repeating-character-replacement/

def character_replacement(s: str, k: int) -> int:
    counts = [0] * 26
    left = 0
    max_freq = 0
    best = 0

    for right, char in enumerate(s):
        idx = ord(char) - ord('A')
        counts[idx] += 1
        max_freq = max(max_freq, counts[idx])

        # If we need more than k changes to unify this window, shrink it
        while (right - left + 1) - max_freq > k:
            counts[ord(s[left]) - ord('A')] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best

# n = len(s)
# O(n) - Time complexity
# O(1) - Space complexity -> fixed 26-size frequency array

print(character_replacement("ABAB", 2)) # 4
print(character_replacement("AABABBA", 1)) # 4