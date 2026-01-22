# Leetcode 1266. Minimum Time Visiting All Points

# https://leetcode.com/problems/minimum-time-visiting-all-points/description/

# Idea
"""
To go from point A(x1, y1) to B(x2, y2) as fast as possible, you should use as many diagonal moves as you can (because one diagonal move changes both x and y by 1 in the same 1 second).

Let:

dx = |x2 - x1|

dy = |y2 - y1|

In min(dx, dy) seconds, you can cover both coordinates via diagonal moves.
Then you have |dx - dy| remaining steps in only one direction (pure horizontal or vertical).

So the minimum time between two consecutive points is:

time
(A → B) = max(dx,dy)

And the answer is the sum over each consecutive pair.
"""
def min_time_visit_points(self, points: list[list[int]]) -> int:
    count = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        count += max(dx, dy)
    return count

# O (n) - Time complexity
# O (1) - Space compexity
