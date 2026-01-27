# Leetcode 1984. Minimum Difference Between Highest and Lowest of K Scores

# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/

# Sliding Window Approach -> Window of k integers
def min_difference(nums: list[int], k: int) -> int:
    if k == 1 or not nums:
        return 0
    
    nums.sort()
    result = float('inf')
    
    for idx in range(len(nums) - k + 1):
        result = min(result, nums[idx + k - 1] - nums[idx])
    return result

# O(n log n) - Time complexity
# O (1) - Space complexity

print(min_difference([90], 1)) # 0
print(min_difference([9,4,1,7], 2)) # 2
