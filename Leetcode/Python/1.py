# Leetcode 1. Two Sum

def solution(nums, target):
  complementDict = {}
  for i, num in enumerate(nums):
    targetSum = target - num
    if targetSum in complementDict:
      return [complementDict[targetSum], i]
    complementDict[num] = i
  return None


print(solution([2, 7, 11, 15], 9))
print(solution([3, 2, 4], 6))
print(solution([3, 3], 6))