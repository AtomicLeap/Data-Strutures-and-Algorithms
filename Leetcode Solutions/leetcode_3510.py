# Leetcode 3510. Minimum Pair Removal to Sort Array II

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/description/

# Key Idea
"""
Because the operation is forced (always merge the adjacent pair with 
minimum sum, leftmost tie), the whole process is deterministic. 
So the “minimum operations” to make the array non-decreasing is simply:

** the first time (earliest step) during this forced merging process when 
the current array becomes non-decreasing.**

We can simulate the merges efficiently with:
1. a min-heap to always pick the current minimum-sum adjacent pair (tie by leftmost),
2. a doubly-linked list over “alive” elements (so we can merge neighbors in O(1)),
3. a counter of “bad adjacent edges” where a > next(a) to know if the array is 
    non-decreasing without scanning every time.

Each merge only affects adjacency near the merged nodes, so the “bad edge” counter 
updates in O(1). Overall: O(n log n).
"""

import heapq
from typing import List

def minimum_operations(nums: List[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    # Doubly-linked list via arrays
    val = nums[:]                       # current value of node i (if alive)
    prev = [i - 1 for i in range(n)]
    nxt  = [i + 1 for i in range(n)]
    nxt[-1] = -1

    alive = [True] * n
    pos = list(range(n))                # left boundary (original index) of this segment
    ver = [0] * n                       # increments whenever node's value or next changes

    def is_bad(i: int, j: int) -> bool:
        return val[i] > val[j]

    # Count initial "bad" adjacent relations
    bad = 0
    for i in range(n - 1):
        if is_bad(i, i + 1):
            bad += 1
    if bad == 0:
        return 0

    # Heap entries: (pair_sum, leftmost_pos, left_id, right_id, verL, verR)
    heap = []
    for i in range(n - 1):
        j = i + 1
        heapq.heappush(heap, (val[i] + val[j], pos[i], i, j, ver[i], ver[j]))

    operations = 0

    while bad > 0:
        # Extract valid current minimum-sum adjacent pair
        while True:
            s, p, i, j, vi, vj = heapq.heappop(heap)
            if not (alive[i] and alive[j]):
                continue
            if nxt[i] != j:  # no longer adjacent
                continue
            if ver[i] != vi or ver[j] != vj:
                continue
            break

        # Neighbors around (i, j)
        a = prev[i]
        b = nxt[j]

        # Remove affected bad-edges BEFORE merge: (a,i), (i,j), (j,b)
        if a != -1 and is_bad(a, i):
            bad -= 1
        if is_bad(i, j):
            bad -= 1
        if b != -1 and is_bad(j, b):
            bad -= 1

        # Merge j into i (i stays as the merged node)
        val[i] = val[i] + val[j]
        ver[i] += 1

        alive[j] = False
        ver[j] += 1

        nxt[i] = b
        if b != -1:
            prev[b] = i

        # Add affected bad-edges AFTER merge: (a,i), (i,b)
        if a != -1 and is_bad(a, i):
            bad += 1
        if b != -1 and is_bad(i, b):
            bad += 1

        operations += 1
        if bad == 0:
            return operations

        # Push updated candidate pairs involving i
        if a != -1:
            heapq.heappush(heap, (val[a] + val[i], pos[a], a, i, ver[a], ver[i]))
        if b != -1:
            heapq.heappush(heap, (val[i] + val[b], pos[i], i, b, ver[i], ver[b]))

    return operations
    
# O(n log n) - Time complexity
# O(n) - Space complexity
