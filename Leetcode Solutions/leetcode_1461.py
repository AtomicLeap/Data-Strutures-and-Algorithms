# Leetcode 1461. Check If a String Contains All Binary Codes of Size K

# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description

# Key observations:
"""
1. If `len(s) < k`, impossible.
2. Even if `len(s) >= k`, you only have `len(s) - k + 1` windows of length `k`.
  If `len(s) - k + 1 < 2^k`, impossible.
3. Since `k ≤ 20`, we can represent each length-`k` substring as an integer 
    in `[0, 2^k - 1]` and use a boolean array (or bitset) to mark seen codes.
4. Use a "rolling bitmask" over the string in O(n) time.
"""

# Rolling bitmask solution

### Idea
"""
1. Maintain an integer `mask` for the last up-to-`k` bits seen while scanning.
2. For each position `i`, shift left, add current bit, and keep only last 
    `k` bits using `& ((1<<k)-1)`.
3. Once `i >= k-1`, `mask` corresponds to the substring `s[i-k+1 .. i]`.

Track unique masks; return `True` as soon as we've seen `2^k` of them.
"""

from typing import List

def has_all_codes(s: str, k: int) -> bool:
    n = len(s)
    if n < k:
        return False

    need = 1 << k
    # Not enough windows to cover all possible codes
    if n - k + 1 < need:
        return False

    seen = [False] * need
    all_ones = need - 1  # bitmask with k ones, e.g. k=3 => 0b111
    mask = 0
    found = 0

    for i, ch in enumerate(s):
        mask = ((mask << 1) & all_ones) | (ch == '1')
        if i >= k - 1:
            if not seen[mask]:
                seen[mask] = True
                found += 1
                if found == need:
                    return True
    return False

# O(n) - Time complexity
# O(2^20) - Space complexity - O(2^k) for seen (max 2^20 ≈ 1,048,576, feasible)


print(has_all_codes("00110110", k = 2)) # True
print(has_all_codes("0110", k = 1)) # True
print(has_all_codes("0110", k = 2)) # False
