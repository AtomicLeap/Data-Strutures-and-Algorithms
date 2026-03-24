# Leetcode 1502. Can Make Arithmetic Progression From Sequence

# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

# Tags -> Array, Sorting

def can_make_arithmetic_progression(arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]

        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False

        return True

# O(n log n) Time complexity, where n is the length of the input array
# O(1) Space complexity 

print(can_make_arithmetic_progression([3,5,1])) # True
print(can_make_arithmetic_progression([1,2,4])) # False
