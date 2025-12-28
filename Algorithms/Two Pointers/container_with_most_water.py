# Leetcode 11. Container With Most Water

# https://leetcode.com/problems/container-with-most-water/description/


# Idea
"""
Area = h_min * (right - left) -> height * Length

Continuously calculate the Area, while persisting the maxArea.
Move pointers on the shorter walls of height[i] and Return the maxArea.
"""

def container_max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        h_min = min(height[left], height[right])
        area = h_min * (right - left)
        max_area = max(max_area, area)
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