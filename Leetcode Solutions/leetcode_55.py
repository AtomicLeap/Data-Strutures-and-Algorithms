# Leetcode 55. Jump Game

# Greedy Algorithm

# https://leetcode.com/problems/jump-game/description/

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

# O(n) - Time complexity
# O(1) - Space complexity

print(jump_game([2,3,1,1,4])) # True
print(jump_game([3,2,1,0,4])) # False
print(jump_game([1,1,0,0,4])) # False
print(jump_game([1,2,2,0,4])) # True