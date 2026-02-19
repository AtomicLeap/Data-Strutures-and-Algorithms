# Leetcode 693. Binary Number with Alternating Bits

# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

def binary_has_alt_bits(n: int) -> bool:
    x = n ^ (n >> 1)
    return (x & (x + 1)) == 0

# O(1) - Time complexity
# O(1) - Space complexity

print(binary_has_alt_bits(5)) # True
print(binary_has_alt_bits(7)) # False
print(binary_has_alt_bits(11)) # False

def binary_has_alt_bits2(n: int) -> bool:
    prev = n & 1
    n >>= 1
    
    while n:
        curr = n & 1
        if curr == prev:
            return False
        prev = curr
        n >>= 1
    
    return True

# O(n log n) - Time complexity
# O(1) - Space complexity

print(binary_has_alt_bits2(5)) # True
print(binary_has_alt_bits2(7)) # False
print(binary_has_alt_bits2(11)) # False