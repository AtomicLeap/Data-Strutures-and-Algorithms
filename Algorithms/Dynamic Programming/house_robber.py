# 198. House Robber

# https://leetcode.com/problems/house-robber/description/

def rob_house(nums: list[int]) -> int:
    skip, take = 0, 0
    for num in nums:
        new_take = skip + num
        new_skip = max(skip, take)
        skip, take = new_skip, new_take
    return max(skip, take)

# O(n) Time complexity
# O(1) Space complexity

print(rob_house([1,2,3,1])) # 4
print(rob_house([2,7,9,3,1])) # 12
print(rob_house([2,1,1,2])) # 4