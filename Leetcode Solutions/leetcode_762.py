# Leetcode 762. Prime Number of Set Bits in Binary Representation

# Bit Manipulation

# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description

# Key Idea
"""
We just need to iterate through the range and count how many numbers 
have a prime popcount (number of 1-bits).

Key observation: right ≤ 10^6 < 2^20, so a number can have at most 20 
set bits. The only primes ≤ 20 are:

{2, 3, 5, 7, 11, 13, 17, 19}

So we can precompute that set and check popcount(x) quickly.
"""

def count_prime_set_bits(left: int, right: int) -> int:
    prime_counts = {2, 3, 5, 7, 11, 13, 17, 19}  # primes up to 20
    result = 0

    for x in range(left, right + 1):
        if x.bit_count() in prime_counts:
            result += 1

    return result

# O(n) - Time complexity
# O(1) - Space complexity

# Using Brian Kernighan’s trick while x: x &= x-1; cnt++
def count_prime_setbits(left: int, right: int) -> int:
    prime_counts = {2, 3, 5, 7, 11, 13, 17, 19}

    def popcount(n: int) -> int:
        c = 0
        while n:
            n &= n - 1  # drops the lowest set bit
            c += 1
        return c

    result = 0
    for x in range(left, right + 1):
        if popcount(x) in prime_counts:
            result += 1
    return result

# O(n) - Time complexity
# O(1) - Space complexity

print(count_prime_set_bits(6, 10)) # 4
print(count_prime_set_bits(10, 15)) # 5

print(count_prime_setbits(6, 10)) # 4
print(count_prime_setbits(10, 15)) # 5