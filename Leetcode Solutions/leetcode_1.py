# Leetcode 1. Two Sum

# https://leetcode.com/problems/two-sum/description/

def solution(nums, target):
  complement_dict = {}
  for i, num in enumerate(nums):
    target_sum = target - num
    if target_sum in complement_dict:
      return [complement_dict[target_sum], i]
    complement_dict[num] = i
  return None

# O(n) - Time complexity
# O(n) - Space complexity

print(solution([2, 7, 11, 15], 9)) # [0, 1]
print(solution([3, 2, 4], 6)) # [1, 2]
print(solution([3, 3], 6)) # [0, 1]
