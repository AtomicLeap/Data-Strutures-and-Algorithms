# Leetcode 55. Jump Game

# Greedy Algorithm

"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


def jump_game(nums):
    max_reach = 0
    last = len(nums) - 1
    
    for i, step in enumerate(nums):
        if i > max_reach:       # 1) If we can't even get to i, we're stuck.
            return False
        max_reach = max(max_reach, i + step)  # 2) Best we can reach so far.
        if max_reach >= last:   # 3) If we can reach/past last index, done.
            return True
    return True                # 4) Finished loop without getting stuck.


# O(n) Time complexity
# O(1) => Space complexity

print(jump_game([2,3,1,1,4])) # True
print(jump_game([3,2,1,0,4])) # False
print(jump_game([1,1,0,0,4])) # False
print(jump_game([1,2,2,0,4])) # True