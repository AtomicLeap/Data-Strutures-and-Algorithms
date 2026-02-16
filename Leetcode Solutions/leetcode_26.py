 # Leetcode 26. Remove Duplicates from Sorted Array

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def solution(nums: list[int]) -> int:
    n = len(nums)
    last_idx = 0 # Last index of unique number

    if not nums:
        return 0
    
    for i in range(1, n):
        if nums[i] != nums[last_idx]:
            nums[last_idx + 1] = nums[i]
            last_idx += 1
    return last_idx + 1

# O(n) - Time complexity
# O(1) - Space complexity

print(solution([1,1,2])) # [1,2,_]
print(solution([0,0,1,1,1,2,2,3,3,4])) # [0,1,2,3,4,_,_,_,_,_]