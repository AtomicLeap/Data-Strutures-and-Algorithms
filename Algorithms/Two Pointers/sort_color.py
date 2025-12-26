# Leetcode 75. Sort Colors

# Dutch National Flag algorithm [three-pointer]

# https://leetcode.com/problems/sort-colors/description/

# 3 Pointer Solution
def sort_colors(nums: list[int]) -> None:
    left, curr, right = 0, 0, len(nums) - 1

    while curr <= right:
        if nums[curr] == 0:
            nums[left], nums[curr] = nums[curr], nums[left]
            left += 1
            curr += 1
        elif nums[curr] == 2:
            nums[right], nums[curr] = nums[curr], nums[right]
            right -= 1
        else:
            curr += 1
    print(f'nums: {nums}')

# O(n) Time complexity
# O(1) Space complexity

sort_colors([2, 0, 2, 1, 1, 0]) # [0, 0, 1, 1, 2, 2]
sort_colors([2, 0, 1]) # [0, 1, 2]
sort_colors([1]) # [1]
sort_colors([2, 1]) # [1, 2]