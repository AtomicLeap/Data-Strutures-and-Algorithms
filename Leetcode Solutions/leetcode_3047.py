# Leetcode 3047. Find the Largest Area of Square Inside Two Rectangles

# https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/description/

# Key Idea
"""
If a square fits inside the intersection of k ≥ 2 rectangles, then it also fits 
inside the intersection of any pair among those rectangles (because the k-way 
intersection is a subset of every pairwise intersection).

So the answer is simply the maximum square area that fits inside the intersection
of any two rectangles.
"""

# How to compute for a pair
"""
For rectangles i and j:
1. Intersection bottom-left: 
    (max(x1i, x1j), max(y1i, y1j))
2. Intersection top-right:
    (min(x2i, x2j), min(y2i, y2j))
Intersection width/height:
    w=min(x2i, x2j) - max(x1i, x1j),h= min(y2i, y2j) - max(y1i, y1j)

If w > 0 and h > 0, they intersect with positive area, and the largest axis-aligned 
square that fits inside has side:
    s = min(w, h)
    Area = s^2
"""

def largest_square_area(bottom_left: list[list[int]], top_right: list[list[int]]) -> int:
    n = len(bottom_left)
    max_area = 0

    for i in range(n):
        x1i, y1i = bottom_left[i]
        x2i, y2i = top_right[i]
        for j in range(i + 1, n):
            x1j, y1j = bottom_left[j]
            x2j, y2j = top_right[j]

            ix1 = max(x1i, x1j)
            iy1 = max(y1i, y1j)
            ix2 = min(x2i, x2j)
            iy2 = min(y2i, y2j)

            w = ix2 - ix1
            h = iy2 - iy1
            if w > 0 and h > 0:
                s = w if w < h else h
                area = s * s
                if area > max_area:
                    max_area = area

    return max_area

# O(n²) - Time complexity
# O(1) - Space complexity

print(largest_square_area([[1,1],[2,2],[3,1]], [[3,3],[4,4],[6,6]])) # 1
print(largest_square_area([[1,1],[1,3],[1,5]], [[5,5],[5,7],[5,9]])) # 4
print(largest_square_area([[1,1],[2,2],[1,2]], [[3,3],[4,4],[3,4]])) # 1
print(largest_square_area([[1,1],[3,3],[3,1]], [[2,2],[4,4],[4,2]])) # 0