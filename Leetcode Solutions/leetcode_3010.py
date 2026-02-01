# Leetcode 3010. Divide an Array Into Subarrays With Minimum Cost I

# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/description

def minimum_cost(nums: list[int]) -> int:
    n = len(nums)
    if n == 3:
        return sum(nums)
    
    min_1 = float('inf')
    min_2 = float('inf')
    for i in range(1, n):
        if nums[i] < min_1:
            min_2 = min_1
            min_1 = nums[i]
        elif min_1 <= nums[i] < min_2:
            min_2 = nums[i]
    return sum((nums[0], min_1, min_2))

# O(n) - Time complexity
# O(1) - Space complexity

print(minimum_cost([1,2,3,12])) # 6
print(minimum_cost([5,4,3])) # 12
print(minimum_cost([10,3,1,1])) # 12