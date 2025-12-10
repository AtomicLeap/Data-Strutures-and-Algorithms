# Leetcode 238. Product of Array Except Self

# https://leetcode.com/problems/product-of-array-except-self/

# Without using division operator
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    results = [1] * n

    # prefix products
    for i in range(1, n):
        results[i] = results[i - 1] * nums[i - 1]

    # suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        results[i] *= suffix
        suffix *= nums[i]

    return results

# O(n) Time complexity
# O(1) Space complexity 

# Examples
print(product_except_self([1,2,3,4]))        # [24, 12, 8, 6]
print(product_except_self([-1,1,0,-3,3]))    # [0, 0, 9, 0, 0]


# Using division operator
def product_except_self_division(nums: list[int]) -> list[int]:
    zero_count = nums.count(0)
    if zero_count > 1:
        return [0] * len(nums)

    # product of non-zero elements
    product = 1
    for num in nums:
        if num != 0:
            product *= num

    if zero_count == 1:
        # only the index with zero gets product; others 0
        return [product if num == 0 else 0 for num in nums]

    # no zeros: safe to divide
    # use integer division; it's exact since nums[i] divides product
    return [product // num for num in nums]

# O(n) Time complexity
# O(1) Space complexity 

# Examples
print(product_except_self_division([1,2,3,4]))        # [24, 12, 8, 6]
print(product_except_self_division([-1,1,0,-3,3]))    # [0, 0, 9, 0, 0]