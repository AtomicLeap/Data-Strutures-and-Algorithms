# Leetcode 3453. Separate Squares I

# https://leetcode.com/problems/separate-squares-i/description

# Key Idea
"""
Because overlaps count multiple times, the squares don't “interact” — 
the area above/below a horizontal line is just the sum of each square's 
cut area. That makes the total area-below function monotone and 
piecewise linear, so we can solve it with a sweep over y-events.

Key idea

For one square with bottom yi and side l:

Let F(y) be the area of this square below the horizontal line at height y.

If y ≤ yi: F(y) = 0
If yi < y < yi + l: F(y) = l * (y - yi) (a rectangle of width l and height y-yi)
If y ≥ yi + l: F(y) = l^2

So for all squares, the total area below the line:

A(y) = ∑Fi(y)

This A(y) is:

1. continuous
2. non-decreasing
3. piecewise linear

We want the minimum y such that:

A(y)= total_area / 2

# Sweep-line view

In the middle region (yi, yi+l), square i contributes slope l to A(y).

So the derivative (slope) is:

A'(y) = ∑ li
        i:yi<y<yi+l

We can maintain this slope using events:

at y = yi : slope += l
at y = yi + l : slope -= l

Between consecutive event y's, slope is constant ⇒ area grows 
linearly ⇒ we can solve the exact y by interpolation.

# Efficient algorithm (O(n log n))

1. Compute total_area = Σ l^2, target half = total_area / 2.
2. Build events {y: delta_slope} for all starts/ends.
3. Sort all event y's.
4. Sweep upward:
	- keep current area_below and current slope
	- for each interval [y0, y1):
		- area increases by slope * (y1 - y0)
		- if target is reached inside, solve:

y = y0 + (half - area_below) / slope

	- also handle flat segments (slope==0) and exact hits at event points 
    to ensure minimum y.
"""

from collections import defaultdict


def separate_squares(squares: list[list[int]]) -> float:
	events = defaultdict(int)  # y -> delta slope
	total_area = 0

	for x, y, l in squares:
		total_area += l * l
		events[y] += l
		events[y + l] -= l

	half = total_area / 2.0
	ys = sorted(events.keys())

	area = 0.0          # A(y0)
	slope = 0.0         # A'(y) on [y0, next_y)
	y0 = ys[0]

	# Before first event, slope is 0 and area is 0; half > 0 so answer won't be below ys[0].
	slope += events[y0]

	eps = 1e-12

	for i in range(len(ys) - 1):
		# At the start of segment, check exact match (gives minimal y)
		if abs(area - half) <= 1e-7:
			return float(y0)

		y1 = ys[i + 1]
		dy = y1 - y0

		if slope > 0:
			next_area = area + slope * dy
			if next_area + eps >= half:
				# Solve within this segment
				return float(y0 + (half - area) / slope)
			area = next_area
		else:
			# slope == 0 => area doesn't change in (y0, y1)
			# if area == half, minimal is y0 already handled above
			pass

		y0 = y1
		slope += events[y0]

	# After last event, area should be total_area (>= half). If half equals area at last point, return it.
	if abs(area - half) <= 1e-7:
		return float(y0)

	# In valid inputs, we should have returned already.
	# Still, safe fallback:
	return float(y0)

# Complexities ->
# Building events: O(n)
# Sorting events (≤ 2n): O(n log n)
# Sweep: O(n)
# Memory: O(n)

print(separate_squares([[0,0,2],[1,1,1]])) # 1.16667
print(separate_squares([[0,0,1],[2,2,1]])) # 1.00000