# Leetcode 137. Single Number II

# https://leetcode.com/problems/single-number-ii/description/

# Bit Counting Method
def single_number(nums: list[int]) -> int:
    result = 0

    for i in range(32):
        bit_sum = 0
        for num in nums:
            if (num >> i) & 1:
                bit_sum += 1

        if bit_sum % 3:
            result |= (1 << i)

    # handle negative numbers (32-bit signed)
    if result >= 2 ** 31:
        result -= 2 ** 32

    return result

# O(n) Time complexity
# O(1) Space complexity


# Finite-State Bitmask Trick

# This is a bitwise state machine solution that tracks counts 
# modulo 3 without loops over bits.

def single_number_i(nums: list[int]) -> int:
    ones = 0
    twos = 0

    for num in nums:
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones

# O(n) Time complexity
# O(1) Space complexity


print(single_number([2,2,3,2])) # 3
print(single_number([0,1,0,1,0,1,99])) # 99
print('-------------------------------')
print(single_number_i([2,2,3,2])) # 3
print(single_number_i([0,1,0,1,0,1,99])) # 99