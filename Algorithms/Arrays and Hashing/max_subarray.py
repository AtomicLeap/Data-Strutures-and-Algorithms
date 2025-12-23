# Leetcode 53. Maximum Subarray

# https://leetcode.com/problems/maximum-subarray/description/

# Kadane algorithm

def max_subarray(nums: list[int]):
    max_sum = curr_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

# O(n) - Time complexity
# O(1) - Space complexity

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(max_subarray([1])) # 1
print(max_subarray([5,4,-1,7,8])) # 23