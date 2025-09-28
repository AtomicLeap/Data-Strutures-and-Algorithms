# Leetcode 190. Reverse Bits

"""
Reverse bits of a given 32 bits signed integer.

Example 1:
Input: n = 43261596
Output: 964176192
Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:
Input: n = 2147483644
Output: 1073741822
Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
 
Constraints:
0 <= n <= 231 - 2
n is even.

Follow up: If this function is called many times, how would you optimize it?
"""

# Key Idea
# Process each of the 32 bits one by one.
# At each step:
# Shift the result left by 1 (res <<= 1).
# Take the least significant bit of n (n & 1) and add it.
# Shift n right by 1 (n >>= 1).
def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)  # append last bit of n to res
        n >>= 1                     # drop last bit of n
    return res

# O(1) - Time complexity
# O(1) - Space complexity


# Follow-up: Multiple Calls Optimization
# If the function is called many times:
# Precompute and cache reversed results for 8-bit numbers (0–255).
# Then reverse a 32-bit integer in 4 lookups + bit shifts.
# Precompute reverse of all 8-bit numbers

reverse_cache = [0] * 256
for i in range(256):
    rev = 0
    x = i
    for _ in range(8):
        rev = (rev << 1) | (x & 1)
        x >>= 1
    reverse_cache[i] = rev

def reverse_bits_opt(n: int) -> int:
    return (
        (reverse_cache[n & 0xff] << 24) |
        (reverse_cache[(n >> 8) & 0xff] << 16) |
        (reverse_cache[(n >> 16) & 0xff] << 8) |
        (reverse_cache[(n >> 24) & 0xff])
    )

# O(1) - Time complexity
# O(1) - Space complexity

print(reverse_bits(43261596)) # 964176192
print(reverse_bits(2147483644)) # 1073741822

print(reverse_bits_opt(43261596)) # 964176192
print(reverse_bits_opt(2147483644)) # 1073741822