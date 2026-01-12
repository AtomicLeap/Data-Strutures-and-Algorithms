# Leetcode 190. Reverse Bits

# https://leetcode.com/problems/reverse-bits/description/

# Key Idea
# Process each of the 32 bits one by one.
# At each step:
# Shift the result left by 1 (result <<= 1).
# Take the least significant bit of n (n & 1) and add it.
# Shift n right by 1 (n >>= 1).
def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)  # append last bit of n to result
        n >>= 1                     # drop last bit of n
    return result

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
    num = i
    for _ in range(8):
        rev = (rev << 1) | (num & 1)
        num >>= 1
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