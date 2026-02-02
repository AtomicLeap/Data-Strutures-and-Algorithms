# Bit manipulation Recipe

# AND (&)
# Compares each bit: result bit = 1 only if both bits are 1.
# → Effect: keeps common 1s.
# Example: 6 & 3 = 2 (110 & 011 = 010).

# OR (|)
# Compares each bit: result bit = 1 if at least one bit is 1.
# → Effect: combines 1s.
# Example: 6 | 3 = 7 (110 | 011 = 111).

# XOR (^)
# Compares each bit: result bit = 1 if bits are different.
# → Effect: highlights differences.
# Example: 6 ^ 3 = 5 (110 ^ 011 = 101).

# Summary in math terms:
# a & b → intersection of bits
# a | b → union of bits
# a ^ b → exclusive difference of bits

# Right shift (>>): 
# Moves all bits to the right, discards the rightmost bit, and fills the 
# left with the sign bit (for signed ints).
# → Effect: Divides by 2 (floor).
# Example: 6 >> 1 = 3 (110 → 011).
# x >> n ≈ x // 2^n (integer division)

# Left shift (<<): 
# Moves all bits to the left, adds 0s on the right.
# → Effect: Multiplies by 2.
# Example: 3 << 1 = 6 (011 → 110).
# x << n ≈ x * 2^n

# So:
# x << n ≈ x * 2^n
# x >> n ≈ x // 2^n (integer division)

# --------------------------------------------------------------------------------------------------- #
# TIPS AND TRICKS

# With AND (&)

# 1. check odd number trick
# If a number has its lowest bit = 1, it’s odd.
# Instead of % 2, you can check:
"""
if n & 1:  # faster than n % 2
    print("Odd")
"""

# 2. Clear the lowest set bit - used to count number of 1's
"""
n = n & (n - 1)
"""
# → Removes the rightmost 1.
# Example: 12 (1100) → 8 (1000).
# Used to count set bits (Brian Kernighan’s algorithm).

# 3. Check if a number is a power of two
"""
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
"""
# (Only powers of two have exactly one set bit).

# 4. Clear the k-th bit
"""
n = n & ~(1 << k)

n = 13 (1101), k = 2
Mask = ~0100 = 1011
1101 & 1011 = 1001 → 9
"""

# 5. Check if k-th bit is set
"""
if n & (1 << k):
    print("Bit is set")
"""

# 6. Check a numbers Lowest set bit

"""
Given number: n

lowest_bit = n & -n
"""

# With OR (|)
# 1. Set a specific bit
"""
n = n | (1 << k)   # set k-th bit to 1
"""
# (1 << k) → makes a mask with only the k-th bit set.
# OR with that mask → guarantees that bit becomes 1, no matter what it was before.

# 2. Force a number to odd
"""
n = n | 1
"""
# 1 in binary = ...0001 (only the least significant bit = 1).
# OR with 1 → ensures the last bit = 1.
# Numbers with last bit = 1 are odd.
# Works even if number was already odd.

# 3. Turn on multiple flags (bitmasking)
# In many systems (OS, databases, games), permissions/features are stored in bits.
# Each bit represents a feature/permission (ON = 1, OFF = 0).

# Example: File permissions
"""
READ  = 1  # 01
WRITE = 2  # 10
perm  = READ | WRITE
print(perm)  # 3
"""
# Binary:
# READ = 01
# WRITE = 10
# 01 | 10 = 11 → 3
# Meaning: permission now has both read and write.

# Real-life analogy
# Think of OR (|) like turning on switches:
# If switch is OFF → it turns ON
# If switch is already ON → it stays ON

# With XOR (^)
# 1. XOR Swap Trick
# You can swap two numbers without using a temporary variable:
"""
a, b = 5, 7
a = a ^ b
b = a ^ b   # (a ^ b) ^ b = a
a = a ^ b   # (a ^ b) ^ a = b
print(a, b)  # 7 5
"""
# Why it works:
# XOR is reversible → x ^ y ^ y = x.

# 2. XOR for Finding Unique Numbers
# In an array where every number appears twice except one, XOR finds the odd one out in O(n):
"""
nums = [2, 3, 2, 4, 4]
result = 0
for num in nums:
    result ^= num
print(result)  # 3
"""
# Why: pairs cancel (x ^ x = 0), leaving the unique element.

# 3. Detect if two numbers differ in parity (odd/even)
# Recall: Odd numbers → binary ends with 1. Even numbers → binary ends with 0
# So we just need to check if last bits differ.
"""
a, b = 7, 4

if (a ^ b) & 1:
    print("Different parity")
else:
    print("Same parity")
"""

# 4. Toggle a specific bit
# XOR flips bits:
# x ^ 1 = ~x (bit is flipped)
# x ^ 0 = x (bit unchanged) --> Identity
# So:
"""
n = n ^ (1 << k)
"""

# 1 << k → creates a mask with only the k-th bit = 1
# XOR with that mask flips that specific bit

# Toggle same bit twice (returns original)
"""
n = 5  # 0101
n = n ^ (1 << 0)  # flip bit 0 → 4
n = n ^ (1 << 0)  # flip bit 0 again → 5
"""

# Toggling twice = no change.

# 5. Check if two numbers are equal
"""
if (a ^ b) == 0:
    print("Equal")
"""

# 6. Find missing number in a sorted array (array 1..n)
"""
def missing_number(nums):
    n = len(nums)
    result = 0
    for i in range(n + 1):
        result ^= i
    for num in nums:
        result ^= num
    return result
"""

# COMBINED Tricks -> With &, |, and ^:
# 1. Isolate lowest set bit
"""
lowbit = n & -n

n = 12  # binary: 1100 
~n = 0011 + 1 = 0100
lowbit = n & -n # 1100 & 0100
print(lowbit)  # 4
"""
# Isolates the lowest set bit.
# Use case: Fenwick Trees (Binary Indexed Trees) use this to find the "range size" controlled by a node.

# 2. Check if two numbers share a set bit
"""
if a & b:
    print("They share a '1' bit")
"""

# Why it works:
# a & b → keeps only common 1s.
# If result ≠ 0, they share at least one set bit.

# 3. Get max without branching
"""
def max_bitwise(a, b):
    return a ^ ((a ^ b) & -(a < b))
"""

# 4. Count set bits (Brian Kernighan’s Algo)
"""
def count_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count
"""

# 5. Check if two numbers have opposite signs
"""
if (a ^ b) < 0:
    print("Opposite signs")
"""
# Because the sign bit differs.

"""
What is XOR?
XOR returns 1 if bits are different, else 0.

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
Core XOR Properties (VERY IMPORTANT)
a ^ a = 0        // duplicates cancel
a ^ 0 = a        // identity
a ^ b = b ^ a    // commutative
(a ^ b) ^ c = a ^ (b ^ c)  // associative
These properties allow us to ignore order and remove duplicates.

When to Use XOR?
Think about XOR when:

1. Every element appears twice except one
2. Exactly two unique elements
3. Asked for O(1) space
4. Bit manipulation tag is present
"""
