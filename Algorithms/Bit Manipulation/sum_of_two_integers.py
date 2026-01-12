# Leetcode 371. Sum of Two Integers

# https://leetcode.com/problems/sum-of-two-integers/description/

def sum_of_ints(a: int, b: int) -> int:
    # 32-bit mask in Python (since Python ints are unbounded)
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        # ^ gets sum without carry
        # & and << gets carry
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # If a is negative, convert from 32-bit unsigned to signed
    return a if a <= MAX_INT else ~(a ^ MASK)

# O(1) - Time complexity -> (at most 32 iterations, since integer is 32-bit)
# O(1) - Space complexity

print(sum_of_ints(1, 2)) # 3
print(sum_of_ints(2, 3)) # 5
print(sum_of_ints(-2, -5)) # -7