# Leetcode 1653. Minimum Deletions to Make String Balanced

# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/description

def min_deletions(s: str) -> int:
    num_of_b = 0          # number of 'b' seen so far
    min_deletions = 0        # min deletions for prefix to be balanced

    for ch in s:
        if ch == 'b':
            num_of_b += 1
        else:  # ch == 'a'
            min_deletions = min(min_deletions + 1, num_of_b)

    return min_deletions

print(min_deletions("aababbab")) # 2
print(min_deletions("bbaaaaabb")) # 2
