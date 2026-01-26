# Leetcode 1877. Minimize Maximum Pair Sum in Array

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/description

def min_pair_sum(nums):
    nums.sort()
    n = len(nums)
    left, right = 0, n - 1
    minified_max_sum = float('-inf')
    while left < right:
        sum_value = nums[left] + nums[right]
        minified_max_sum = sum_value if sum_value > minified_max_sum else minified_max_sum
        left += 1
        right -= 1
    return minified_max_sum

# O(n log n) - Time complexity
# O(1) - Space complexity

print(min_pair_sum([3,5,2,3])) # 7
print(min_pair_sum([3,5,4,2,4,6])) # 8