# Leetcode 2943. Maximize Area of Square Hole in Grid

# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description

# Key Idea
"""
Removing one horizontal bar merges two adjacent 1x1 cells vertically, giving height 2.
Removing k consecutive horizontal bars merges k+1 cells vertically, giving height k+1.

So:
Maximum possible hole height = 1 + (longest consecutive run in hBars)
Maximum possible hole width = 1 + (longest consecutive run in vBars)

To form the largest square hole, the side length is limited by the smaller of those two:

    side = min(maxHeight, maxWidth)   ⇒   area = side^2

Because hBars.length, vBars.length ≤ 100, sorting + a linear scan is plenty fast.

Algorithm:
Sort hBars, compute the longest streak of consecutive integers (difference = 1).
Sort vBars, compute the longest streak similarly.
maxHeight = 1 + bestRunH, maxWidth = 1 + bestRunV
side = min(maxHeight, maxWidth), return side * side
"""

def maximize_square_hole_area(n: int, m: int, h_bars: list[int], v_bars: list[int]) -> int:
    def longest_consecutive_run(bars: list[int]) -> int:
        bars.sort()
        best = 1
        cur = 1
        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                cur += 1
            else:
                cur = 1
            best = max(best, cur)
        return best  # run length in "removed bars"

    h_run = longest_consecutive_run(h_bars)
    v_run = longest_consecutive_run(v_bars)

    max_height = 1 + h_run
    max_width  = 1 + v_run

    side = min(max_height, max_width)
    return side * side

# O(H log H + V log V) (H, V ≤ 100) - Time complexity
# O(1) extra (ignoring sort cost) - Space complexity

print(maximize_square_hole_area(2, 1, [2,3], [2])) # 4
print(maximize_square_hole_area(1, 1, [2], [2])) # 4
print(maximize_square_hole_area(2, 3, [2,3], [2,4])) # 4