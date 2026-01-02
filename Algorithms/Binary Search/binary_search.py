# Leetcode 704. Binary Search

# https://leetcode.com/problems/binary-search/description/

# Search for a target in sorted list - Classic Binary Search
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(log n) - Time complexity
# O(1) - Space complexity

print(search([-1,0,3,5,9,12], 9)) # 4
print(search([-1,0,3,5,9,12], 2)) # -1
