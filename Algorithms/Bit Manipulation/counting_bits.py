# Leetcode 338. Counting Bits

# https://leetcode.com/problems/counting-bits/

# Idea, Use the relation:
# bits[i] = bits[i >> 1] + (i & 1)
# Right-shift drops the least significant bit; (i & 1) adds 1 if i is odd.
def count_bits(n: int):
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        table[i] = table[i >> 1] + (i & 1)
    return table

# O(n) - Time complexity -> where b is the number of bits, still efficient in practice.
# O(n) - Space complexity -> for the output array


# Clear lowest set bit ->
# n = n & (n - 1)
def count_bits_alt(n: int):
    table = [0] * (n + 1)
    for i in range(1, n + 1):
        table[i] = table[i & (i - 1)] + 1
    return table

# O(n) - Time complexity -> where b is the number of bits, still efficient in practice.
# O(n) - Space complexity -> for the output array

print(count_bits(2)) # [0,1,1]
print(count_bits(5)) # [0,1,1,2,1,2]
print(count_bits(25))

print(count_bits_alt(2)) # [0,1,1]
print(count_bits_alt(5)) # [0,1,1,2,1,2]
print(count_bits(25))
