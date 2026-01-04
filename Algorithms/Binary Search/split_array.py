# Leetcode 410. Split Array Largest Sum

# https://leetcode.com/problems/split-array-largest-sum/description/

# Idea
"""
1. Design a feasible function: given an input threshold, then decide if we can 
    split the array into several subarrays such that every subarray-sum is 
    less than or equal to threshold. In this way, we discover the monotonicity 
    of the problem: if feasible(m) is True, then all inputs larger than m can 
    satisfy feasible function.
2. Threshold should be at least max(nums) and atmost sum(nums).
"""

def split_array(nums: list[int], k: int) -> int:    
    def feasible(threshold: int) -> bool:
        count = 1
        total = 0
        for num in nums:
            total += num
            if total > threshold:
                total = num
                count += 1
                if count > k:
                    return False
        return True

    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid     
        else:
            left = mid + 1
    return left

# O(n) - Time complexity
# O(1) - Space complexity


print(split_array([7,2,5,10,8], 2)) # 18
print(split_array([1,2,3,4,5], 2)) # 9