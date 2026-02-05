# Leetcode 3637. Trionic Array I

# https://leetcode.com/problems/trionic-array-i/description

def is_trionic(nums: list[int]) -> bool:
    n = len(nums)

    p = 0

    #1. Strictly increasing check
    while p < n - 2 and nums[p] < nums[p + 1]:
        p += 1
    if p == 0:
        return False

    q = p
    #2.  Strictly decreasing check
    while q < n - 1 and nums[q] > nums[q + 1]:
        q += 1
    if q == p or q == n - 1:
        return False
    
    #3. Strictly increasing check
    while q < n - 1 and nums[q] < nums[q + 1]:
        q += 1
    
    return q == n - 1

# O(n) - Time complexity
# O(1) - Space complexity

print(is_trionic([1,3,5,4,2,6])) # True
print(is_trionic([2,1,3])) # False
