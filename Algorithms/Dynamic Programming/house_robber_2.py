# 213. House Robber II

# https://leetcode.com/problems/house-robber-ii/description/

# Idea (why the circle matters)
# In the linear version, you can’t rob adjacent houses. With a circle, the first and 
# last are also adjacent, so you can’t take both.
# Key trick: split into two linear cases and take the best:
# Rob houses 0 .. n-2 (exclude last)
# Rob houses 1 .. n-1 (exclude first)
# Answer = max(rob_linear(nums[0:n-1]), rob_linear(nums[1:n]))

# If n == 1, the answer is just nums[0].

def _rob_house_helper(nums: list[int]) -> int:
    skip, take = 0, 0

    for num in nums:
        new_take = skip + num
        new_skip = max(skip, take)
        take, skip = new_take, new_skip
    return max(skip, take)

def rob_house_cycle(nums: list[int]) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    return max(_rob_house_helper(nums[:-1]), _rob_house_helper(nums[1:]))

# O(n) Time complexity
# O(1) Space complexity

print(rob_house_cycle([2,3,2])) # 3
print(rob_house_cycle([1,2,3,1])) # 4
print(rob_house_cycle([1,2,3])) # 3