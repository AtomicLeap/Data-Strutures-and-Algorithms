# Leetcode 761. Special Binary String

# https://leetcode.com/problems/special-binary-string/description

def make_largest_special(s: str) -> str:
    # Base case: too short to change
    if len(s) <= 2:
        return s

    parts = []
    balance = 0
    start = 0

    # Split into top-level special substrings
    for i, char in enumerate(s):
        balance += 1 if char == '1' else -1
        if balance == 0:
            # s[start:i+1] is a top-level special block: 1 ... 0
            inner = s[start + 1:i]  # strip outer 1 and 0
            best_inner = make_largest_special(inner)
            parts.append("1" + best_inner + "0")
            start = i + 1

    # Sort blocks descending to maximize lexicographic order
    parts.sort(reverse=True)
    return "".join(parts)

# OO(n^2. log n) - Time complexity
# O(n^2) - Space complexity

print(make_largest_special("11011000")) # "11100100"
print(make_largest_special("10")) # "10"
