# Leetcode 1356. Sort Integers by The Number of 1 Bits

# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description

# Tags -> Arrays, Bit Manipulation, Sorting

def sort_by_bits(arr: list[int]) -> list[int]:
    # popcount helper (works on all Python 3 versions)
    def set_bit_count(num: int) -> int:
        count = 0
        while num:
            num &= num - 1   # drop lowest set bit
            count += 1
        return count

    return sorted(arr, key=lambda x: (set_bit_count(x), x))

print(sort_by_bits([0,1,2,3,4,5,6,7,8])) # [0,1,2,4,8,3,5,6,7]
print(sort_by_bits([1024,512,256,128,64,32,16,8,4,2,1])) # [1,2,4,8,16,32,64,128,256,512,1024]

# Using Python built-in bit_count function
def sort_by_bits_b(arr: list[int]) -> list[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))

# O(n.log n) - Time complexity
# O(n) - Space complexity

print(sort_by_bits_b([0,1,2,3,4,5,6,7,8])) # [0,1,2,4,8,3,5,6,7]
print(sort_by_bits_b([1024,512,256,128,64,32,16,8,4,2,1])) # [1,2,4,8,16,32,64,128,256,512,1024]