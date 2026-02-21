# Leetcode 3454. Separate Squares II

# https://leetcode.com/problems/separate-squares-ii/description/

# Tags -> Segment Tree, Binary Search

from typing import List, Tuple
from collections import defaultdict

class SegTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1  # number of elementary segments
        self.count = [0] * (4 * self.n)
        self.covered = [0] * (4 * self.n)

    def _pull(self, idx: int, l: int, r: int):
        if self.count[idx] > 0:
            # fully covered
            self.covered[idx] = self.xs[r + 1] - self.xs[l]
        elif l == r:
            self.covered[idx] = 0
        else:
            self.covered[idx] = self.covered[idx * 2] + self.covered[idx * 2 + 1]

    def _update(self, idx: int, l: int, r: int, ql: int, qr: int, delta: int):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self.count[idx] += delta
            self._pull(idx, l, r)
            return
        mid = (l + r) // 2
        self._update(idx * 2, l, mid, ql, qr, delta)
        self._update(idx * 2 + 1, mid + 1, r, ql, qr, delta)
        self._pull(idx, l, r)

    def update_interval(self, x1_idx: int, x2_idx: int, delta: int):
        # updates [x1_idx, x2_idx-1] in elementary segment indices
        if x1_idx <= x2_idx - 1:
            self._update(1, 0, self.n - 1, x1_idx, x2_idx - 1, delta)

    def covered_length(self) -> int:
        return self.covered[1] if self.n > 0 else 0


def split_union_area_y(squares: List[List[int]]) -> float:
    # Build events and x-coordinates
    events = defaultdict(list)  # y -> list of (x1, x2, delta)
    xs = []
    for x, y, l in squares:
        x1, x2 = x, x + l
        y1, y2 = y, y + l
        xs.append(x1); xs.append(x2)
        events[y1].append((x1, x2, +1))
        events[y2].append((x1, x2, -1))

    xs = sorted(set(xs))
    if len(xs) == 1:
        # all squares have zero width? impossible since l>=1, but safe
        return float(min(y for _, y, _ in squares))

    # map x -> index in xs
    x_to_i = {v: i for i, v in enumerate(xs)}

    ys = sorted(events.keys())
    st = SegTree(xs)

    # Sweep once, recording slabs: (y, next_y, covered_len, area_prefix_at_y)
    slabs: List[Tuple[int, int, int, int]] = []
    area_prefix = 0

    for i, y in enumerate(ys):
        # apply all events at this y
        for x1, x2, d in events[y]:
            st.update_interval(x_to_i[x1], x_to_i[x2], d)

        if i + 1 == len(ys):
            break
        ny = ys[i + 1]
        L = st.covered_length()
        dy = ny - y
        slabs.append((y, ny, L, area_prefix))
        area_prefix += L * dy

    total_area = area_prefix
    if total_area == 0:
        # No union area (shouldn't happen with positive l), but define as min y.
        return float(min(y for _, y, _ in squares))

    # Find minimal y with area_below == total_area / 2
    # Use integer arithmetic with "target2 = total_area" representing 2*(total_area/2).
    target2 = total_area  # equals 2 * half area when comparing against 2*prefix

    for y, ny, L, pref in slabs:
        # We want 2*(pref + L*delta) == total_area  for some delta in [0, ny-y]
        need = target2 - 2 * pref

        if need == 0:
            # Already exactly half at slab start; minimal y is this y
            return float(y)

        if L == 0:
            # area doesn't change in this slab
            continue

        # Check if half lies within this slab:
        # At end: 2*(pref + L*(ny-y)) = 2*pref + 2*L*dy
        dy = ny - y
        end2 = 2 * pref + 2 * L * dy

        if (2 * pref < target2 <= end2) or (end2 <= target2 < 2 * pref):
            # Solve delta = (target2 - 2*pref) / (2*L)
            delta = (target2 - 2 * pref) / (2.0 * L)
            # Clamp for safety
            if delta < 0:
                delta = 0.0
            elif delta > dy:
                delta = float(dy)
            return y + delta

    # If we didn't return inside slabs, half must be at/after last y (numerically)
    return float(ys[-1])


# Example usage:
print(f"{split_union_area_y([[0,0,1],[2,2,1]]):.5f}")  # 1.00000
print(f"{split_union_area_y([[0,0,2],[1,1,1]]):.5f}")  # 1.00000


# O(n* log n) - Time complexity
# O(n) - Space complexity

