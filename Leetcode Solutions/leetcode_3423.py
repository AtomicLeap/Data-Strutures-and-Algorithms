# Leetcode 3423. Maximum Difference Between Adjacent Elements in a Circular Array

# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description

# Tags -> Array, Greedy

# Idea
"""
To find the maximum difference between adjacent elements in a 
circular array, we can iterate through the array and calculate the 
difference between each pair of adjacent elements. We also need to 
consider the difference between the last and the first element 
since it's a circular array. We can keep track of the maximum 
difference found during the iteration and return it at the end.
"""

def max_circular_adjacent_diff(nums: list[int]) -> int:
    max_diff = 0
    n = len(nums)
    
    for i in range(n):
        diff = abs(nums[i] - nums[(i + 1) % n])
        max_diff = max(max_diff, diff)
    
    return max_diff

# O(n) Time complexity
# O(1) Space complexity

print(max_circular_adjacent_diff([1,2,4])) # 3
print(max_circular_adjacent_diff([-5,-10,-5])) # 5
print(max_circular_adjacent_diff([1,5,3,8])) # 7


def max_adjacent_distance(nums: list[int]) -> int:
    max_dist = float('-inf')
    n = len(nums)
    
    for i in range(1, n):
        diff = abs(nums[i] - nums[i - 1])
        max_dist = max(max_dist, diff)
    max_dist = max(max_dist, abs(nums[0] - nums[-1]))
    
    return max_dist

# O(n) Time complexity
# O(1) Space complexity

print(max_circular_adjacent_diff([1,2,4])) # 3
print(max_circular_adjacent_diff([-5,-10,-5])) # 5
print(max_circular_adjacent_diff([1,5,3,8])) # 7
