# Leetcode 191. Number of 1 Bits

# https://leetcode.com/problems/number-of-1-bits/

# this is Hamming weight (number of 1s in the binary representation).

# Efficient Bit Manipulation — Brian Kernighan’s Algorithm
# n = n & (n - 1) -> remove a set bit
def number_of_1bits(n: int) -> int:
    count = 0
    while n:
        n &= n - 1  # clears the lowest set bit
        count += 1
    return count

# O(k) - Time complexity -> where k = number of set bits, much faster than looping over all 32 bits.
# O(1) - Space complexity

print(number_of_1bits(11))
print(number_of_1bits(128))
print(number_of_1bits(2147483645))

# Built-in Python Optimization
def hamming_weight(n: int) -> int:
    return bin(n).count("1")

# O(b) - Time complexity -> where b is the number of bits, still efficient in practice.
# O(1) - Space complexity

print(hamming_weight(11))
print(hamming_weight(128))
print(hamming_weight(2147483645))

# Follow-up: Optimize for Many Calls

# Solution 1
# If the function is called millions of times:
# Precompute for bytes (0–255):
# Store the number of set bits for each possible byte in a lookup table.
# Then process the number 8 bits at a time using bit shifts.
# Precompute lookup for 8-bit numbers

lookup = [bin(i).count("1") for i in range(256)]

def hamming_weight_opt1(n: int) -> int:
    count = 0
    while n:
        count += lookup[n & 0xFF]  # take last 8 bits
        n >>= 8
    return count

# Solution 2
def hamming_weight_opt2(n: int) -> int:
    return n.bit_count()

def bit_count(num):
    count = 0
    binary = bin(num)

    for digit in binary:
        if digit == '1':
            count += 1
    return count