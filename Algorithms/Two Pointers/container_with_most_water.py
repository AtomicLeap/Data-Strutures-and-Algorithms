# Leetcode 11. Container With Most Water

"""
You are given an integer array height of length n. There are n vertical lines drawn 
such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container
contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

# Area = h_min * (right - left) -> height * Length
def container_max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h_min = min(height[left], height[right])
        max_area = max(max_area, h_min * (right - left))
        # Move the pointer at the shorter wall
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

# O(n) - Time complexity
# O(1) - Space complexity

print(container_max_area([1,8,6,2,5,4,8,3,7])) # 49
print(container_max_area([1,1])) # 1