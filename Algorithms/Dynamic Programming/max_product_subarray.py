# Leetcode 152. Maximum Product Subarray

# https://leetcode.com/problems/maximum-product-subarray/description/

def max_subarray(nums: list[int]) -> int:
    max_value = min_value = result = nums[0]

    for num in nums[1:]:
        if num < 0:
            max_value, min_value = min_value, max_value
        
        max_value = max(num, max_value * num)
        min_value = max(num, min_value * num)

        result = max(result, max_value)
    return result

# O(n) Time complexity
# O(1) Space complexity

print(max_subarray([2,3,-2,4])) # 6
print(max_subarray([-2,0,-1])) # 0
