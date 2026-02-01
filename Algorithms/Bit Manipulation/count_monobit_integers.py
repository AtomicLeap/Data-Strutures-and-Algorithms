# Leetcode 3827. Count Monobit Integers

# https://leetcode.com/problems/count-monobit-integers/description/

# Key Idea
"""
A Monobit integer has a binary representation (with no leading zeros, except 0 itself) 
where all bits are identical.

That means the only possibilities are:

1. 0 → "0"
2. Numbers with all 1s:
1 (1), 3 (11), 7 (111), 15 (1111), …
i.e. numbers of the form 2^k - 1 for k >= 1

There are no positive Monobit numbers made of all 0s, because leading zeros are not allowed.

So we need to count how many values of 
    2^k - 1 <= n => 2^k <= n + 1 => k <= |log2(n + 1)|

Answers are:
1. Always count 0 → 1 
2. Plus floor(log2(n+1)) many “all-ones” numbers
"""

def count_monobit_integer(n: int) -> int:
    # 0 is always monobit ("0")
    # Count of (2^k - 1) <= n => floor(log2(n+1))
    return 1 + (n + 1).bit_length() - 1

# O(1) - Time complexity
# O(1) - Space complexity

print(count_monobit_integer(1)) # 2
print(count_monobit_integer(4)) # 3
