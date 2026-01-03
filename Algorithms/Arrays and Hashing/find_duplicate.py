# Leetcode 287. Find the Duplicate Number

# https://leetcode.com/problems/find-the-duplicate-number/description/

# Use Floyd’s Tortoise and Hare algorithm (2-Pointer Fast and Slow Algorithm)
def find_duplicate(nums: list[int]) -> int:
    # Phase 1: find intersection point in the cycle
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find entrance to the cycle (duplicate)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# O(n) - Time complexity
# O(1) - Space complexity

print(find_duplicate([1,3,4,2,2])) # 2
print(find_duplicate([3,1,3,4,2])) # 3
print(find_duplicate([3,3,3,3,3])) # 3