# Leetcode 191. Number of 1 Bits

"""
Given a positive integer n, write a function that returns the number of set bits in its 
binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:

The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:
1 <= n <= 231 - 1
Follow up: If this function is called many times, how would you optimize it?
"""
# this is Hamming weight (number of 1s in the binary representation).

# Efficient Bit Manipulation — Brian Kernighan’s Algorithm
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

