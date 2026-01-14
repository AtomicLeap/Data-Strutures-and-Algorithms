# Leetcode 85. Maximal Rectangle

# https://leetcode.com/problems/maximal-rectangle/description/

# Key Idea
"""
1. Key idea (turn 2D → many 1D histograms)
2. Treat each row as the “base” of a histogram:
3. Maintain an array heights[j] = number of consecutive '1's ending at 
    current row in column j.

For each row:
If matrix[i][j] == '1', heights[j] += 1
Else heights[j] = 0

Now the largest all-1s rectangle ending at this row is exactly the 
Largest Rectangle in Histogram on heights.

Take the max across all rows.

This gives O(rows * cols) time because each histogram solve is O(cols) with a monotonic stack.
"""

def maximal_rectangle(matrix: list[list[str]]) -> int:
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area_of_one = 0

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "1":
                heights[col] += 1
            else:
                heights[col] = 0
        max_area_of_one = max(max_area_of_one, _largest_rectangle(heights))
    return max_area_of_one

def _largest_rectangle(heights: list[int]) -> int:
    stack = []
    max_area = 0

    for idx, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] > height:
            last_height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = idx - left - 1
            area = last_height * width
            max_area = max(max_area, area)
        stack.append(idx)
    return max_area

# r, c = len(rows), len(cols)
# O(r * c) Time complexity
# O(c) Space complexity 

print(maximal_rectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])) # 6
print(maximal_rectangle([["0"]])) # 0
print(maximal_rectangle([["1"]])) # 1