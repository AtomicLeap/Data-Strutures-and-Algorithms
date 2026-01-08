# Leetcode 260. Single Number III

# https://leetcode.com/problems/single-number-iii/description/

def single_number(nums: list[int]) -> list[int]:
    # Step 1: XOR of all elements = x ^ y
    xor_result = 0 # Zero is Identity of XOR

    for num in nums:
        xor_result ^= num

    # Step 2: isolate rightmost set bit
    diff_bit = xor_result & -xor_result

    # Step 3: partition to 2 groups and XOR
    single_1 = 0
    single_2 = 0

    for num in nums:
        if num & diff_bit:
            single_1 ^= num
        else:
            single_2 ^= num
    return [single_1, single_2]

# O(n) Time complexity
# O(1) Space complexity


print(single_number([1,2,1,3,2,5])) # [3, 5]
print(single_number([-1,0])) # [-1,0]
print(single_number([0,1])) # [1, 0]