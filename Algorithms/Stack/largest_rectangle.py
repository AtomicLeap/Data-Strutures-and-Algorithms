# Leetcode 84. Largest Rectangle in Histogram

# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

# Key Idea
"""
Use a monotonic increasing stack of indices. The key idea:
1. Keep indices of bars in non-decreasing height order.
2. When you see a bar shorter than the stack top, the stack top bar 
    can no longer extend to the right, so you pop it and compute the 
    max rectangle where that popped bar is the minimum height.

For a popped index mid:
- h = heights[mid]
- right boundary = current index i (exclusive)
- left boundary = new stack top after popping (exclusive), or -1 if empty
- width = i - left - 1
- area = h * width

To flush remaining bars, append a sentinel 0 height at the end.
"""

def largest_rectangle_in_histogram(heights: list[int]) ->int:
    stack = []
    max_area = 0

    for idx, height in enumerate(heights + [0]):
        while stack and height < stack[-1][1]:
            _, last_height = stack.pop()
            left = stack[-1][0] if stack else -1
            width = idx - left - 1 # idx = right
            area = width * last_height
            max_area = max(area, max_area)
        stack.append((idx, height))
    return max_area

# n = len(s)
# O(n) Time complexity
# O(n) Space complexity 

print(largest_rectangle_in_histogram([2,1,5,6,2,3])) # 10
print(largest_rectangle_in_histogram([2,4])) # 4

# Appending indices only to Stack
def largest_rectangle_in_histogram_i(heights: list[int]) ->int:
    stack = []
    max_area = 0

    for idx, height in enumerate(heights + [0]):
        while stack and height < heights[stack[-1]]:
            last_idx = stack.pop()
            left = stack[-1] if stack else -1
            width = idx - left - 1 # idx = right
            area = width * heights[last_idx]
            max_area = max(area, max_area)
        stack.append(idx)
    return max_area

# O(n) Time complexity
# O(n) Space complexity 

print(largest_rectangle_in_histogram_i([2,1,5,6,2,3])) # 10
print(largest_rectangle_in_histogram_i([2,4])) # 4