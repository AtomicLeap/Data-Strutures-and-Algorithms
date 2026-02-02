# Intervals Recipe

"""
Intervals show up whenever you're reasoning about ranges on a line: 
time windows, meeting bookings, segments on a number line, start/end 
indices, reservations, coverage, collisions, etc. Most interval problems 
reduce to a small set of patterns.
"""

# Core representation

"""
An interval is usually [start, end] (often inclusive). Sometimes it's 
[start, end) (end-exclusive). That detail changes comparisons:

1. Overlap (inclusive): [a,b] overlaps [c,d] if a <= d && c <= b
2. Overlap (half-open): [a,b) overlaps [c,d) if a < d && c < b

Always check what the problem means by “overlap” (touching endpoints may 
or may not count).
"""

# The 8 interval patterns

"""
1) Sort + merge (Merge Intervals)
Goal: combine overlapping intervals into disjoint merged intervals.

Idea: sort by start, then sweep and extend the current interval.

Example
Input: [[1,3],[2,6],[8,10],[15,18]]
Sorted: same
Merge result: [[1,6],[8,10],[15,18]]

Why it works: once sorted by start, any overlap with the current merged 
interval must be with the “latest” end so far.
"""
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    results = []
    for s, e in intervals:
        if not results or s > results[-1][1]:
            results.append([s, e])
        else:
            results[-1][1] = max(results[-1][1], e)
    return results

# 2) Insert interval (Insert + merge)

"""
Goal: insert a new interval into a set of non-overlapping sorted intervals.

Idea: copy intervals that end before new, merge overlaps, then append rest.

Example
Intervals: [[1,2],[3,5],[6,7],[8,10],[12,16]], new [4,8]
Result: [[1,2],[3,10],[12,16]]
"""

def insert(intervals, new_interval):
    ns, ne = new_interval
    results = []
    i = 0
    n = len(intervals)

    while i < n and intervals[i][1] < ns:
        results.append(intervals[i]); i += 1

    while i < n and intervals[i][0] <= ne:
        ns = min(ns, intervals[i][0])
        ne = max(ne, intervals[i][1])
        i += 1
    results.append([ns, ne])

    while i < n:
        results.append(intervals[i]); i += 1
    return results

# 3) Meeting rooms / minimum number of resources

"""
Goal: given meetings, find minimum rooms needed.

Two standard solutions:
"""
# A) Min-heap of end times (classic)

"""
Sort by start, keep a min-heap of current end times.

If earliest end <= current start, reuse room (pop)

Else need a new room (push)

"""

import heapq

def min_rooms(intervals):
    intervals.sort(key=lambda x: x[0])
    heap = []
    for s, e in intervals:
        if heap and heap[0] <= s:
            heapq.heappop(heap)
        heapq.heappush(heap, e)
    return len(heap)

# B) Sweep line with “events”

"""
Turn each interval into (start, +1) and (end, -1) then prefix-sum max.
Careful with tie-breaking: if touching is allowed (end at 10, start at 10 
doesn't overlap), process end before start at same time.
"""

# 4) Interval scheduling (pick max non-overlapping)

"""
Goal: select maximum number of non-overlapping intervals.

Greedy rule: sort by end time, always pick the earliest finishing 
compatible interval.

Example
[[1,4],[3,5],[0,6],[5,7],[8,9]]
Pick [1,4], then [5,7], then [8,9] ⇒ 3

Why it works: earliest finish leaves most room for future intervals.
"""

def max_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_end = float("-inf")
    for s, e in intervals:
        if s >= last_end:
            count += 1
            last_end = e
    return count

# 5) Minimum intervals to remove (erase overlap)

"""
Goal: remove minimum intervals so the rest don't overlap.

Equivalent to: keep maximum non-overlapping.
Answer = n - max_non_overlapping.
"""

# 6) Coverage / “can we cover [L,R]?” (Greedy coverage)

"""
Goal: choose as few intervals as possible to cover a target range.

Greedy rule: at position curr, among intervals with start <= curr, take the one with farthest end.

This is the same idea as “Jump Game” but with ranges.
"""

# 7) Intersections (two lists)

"""
Goal: intersection of two sorted disjoint interval lists.

Idea: two pointers.
Overlap is max(starts) to min(ends) if valid.
"""

def intersect(A, B):
    i = j = 0
    results = []
    while i < len(A) and j < len(B):
        s = max(A[i][0], B[j][0])
        e = min(A[i][1], B[j][1])
        if s <= e:
            results.append([s, e])
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    return results

# 8) “Range add” / “how many overlaps at each point?” 
# (Difference array / sweep line)

"""
Goal: count coverage, max overlap, build merged coverage length, etc.
Technique: event map / difference array

diff[start] += 1

diff[end] -= 1 (tie depends on inclusivity)
Then sort keys and accumulate.

This generalizes to weighted overlaps too.
"""

# Decision cheat-sheet (how to recognize the right tool)

"""
1. Need merged disjoint output → sort by start + merge
2. Need detect overlaps / conflicts → sort by start + compare ends
3. Need max compatible set → sort by end + greedy
4. Need min resources simultaneously → heap of end times OR sweep line events
5. Need intersection of 2 lists → two pointers
6. Need “how many active at time t / max overlap” → sweep line / diff map
7. Need dynamic queries (insert/delete intervals, query overlap) → balanced BST / interval tree (advanced)
"""

# Common pitfalls

"""
1. Inclusive vs exclusive endpoints (touching counts?)
2. Sorting key: merge uses start, scheduling uses end
3. In sweep line, tie-breaking at same coordinate is everything
4. Large coordinate ranges: use coordinate compression + diff array or map
"""

# High-yield practice problems (by pattern)

"""
1. Merge Intervals
2. Insert Interval
3. Non-overlapping Intervals (remove min)
4. Meeting Rooms I/II
5. Interval List Intersections
6. Minimum Number of Arrows to Burst Balloons (end-time greedy)
7. Car Pooling (diff/sweep)
8. Employee Free Time (merge + gaps)
"""

# The 6 patterns that solve ~90% of interval problems

# 1) Sort by start → Merge / Union

"""
Use when: output needs merged intervals, or you're simplifying overlaps.

Template
1. sort by start
2. keep cur=[s,e]
3. if next starts after cur.end → push cur
    else merge by cur.end=max(cur.end,next.end)
"""

# Must-do problems

"""
56. Merge Intervals
57. Insert Interval (same idea + “before/overlap/after” split)
228. Summary Ranges (1D merging variant)
252/253 (meeting rooms uses sorting too)
"""

# 2) Sort by end → Greedy selection / remove overlaps

"""
Use when: “maximum number of non-overlapping intervals” or “minimum removals”.
Why end-time? earliest finish leaves maximum room.

Template

1. sort by end
2. take interval if start >= last_end
    else skip/remove
"""
# Must-do problems

"""
435. Non-overlapping Intervals (min removals)
452. Minimum Number of Arrows to Burst Balloons (same greedy)
1288. Remove Covered Intervals (needs careful sort, see below)
"""

# 3) Min-heap of end times → Min rooms/resources

"""
Use when: “minimum number of groups/rooms/resources” for overlaps.

Template

1. sort by start
2. heap stores end times of active intervals
3. if smallest end <= current start → pop (reuse)
4. push current end
5. heap size = rooms
"""

# Must-do problems

"""
253. Meeting Rooms II
2406. Divide Intervals Into Minimum Number of Groups (very similar)
1094. Car Pooling can be heap, but sweep is cleaner
"""

# 4) Sweep line / difference array → count overlaps, capacity, max concurrency

"""
Use when: you care about “how many active” over time, max overlap, 
capacity constraints.

Events
-> (start, +1)
-> (end, -1)
    Tie-breaking matters:
-> If touching is not overlap (end==start is OK), process end before 
    start at same time.
"""
# Must-do problems

"""
1094. Car Pooling (difference array)
1109. Corporate Flight Bookings (difference array)
1854. Maximum Population Year (events)
732. My Calendar III (hard; sweep/BST map)
"""

# 5) Two pointers → Intersection of two interval lists

"""
Use when: two sorted, disjoint lists and you need overlaps.

Template
1. i,j
2. overlap is [max(a.start,b.start), min(a.end,b.end)] if valid
3. advance pointer with smaller end
"""

# Must-do problems

"""
986. Interval List Intersections
"""

# 6) “Cover a target range” greedy → take farthest reach

"""
Use when: cover [L,R] with minimum intervals (classic coverage).

Template
1. sort by start
2. maintain curr and best_end
3. among intervals with start <= curr, extend best_end=max(best_end,end)
4. when you must commit, set curr=best_end, count++

"""

# Must-do problems

"""
1024. Video Stitching
45. Jump Game II (same greedy idea, not intervals but same skeleton)
"""

# Decision Guide

"""
1. Need merged output? → sort by start + merge
2. Need max non-overlap / min removals / arrows? → sort by end + greedy
3. Need min # rooms/groups? → heap of ends OR sweep line
4. Need max overlap / capacity feasibility? → sweep/diff
5. Need intersection of two lists? → two pointers
6. Need cover [0,T] or [L,R]? → farthest-reach greedy
"""

# Leetcode “Intervals Study Path”

"""
Level 1 (core)

56 Merge Intervals
57 Insert Interval
435 Non-overlapping Intervals
452 Minimum Arrows
986 Interval List Intersections
1288. Remove Covered Intervals

Level 2 (counting + resources)
6. 253 Meeting Rooms II
7. 1094 Car Pooling
8. 1109 Corporate Flight Bookings

Level 3 (hard patterns)
9. 1024 Video Stitching
10. 732 My Calendar III (sweep map / segment tree variants)
"""

# Core Templates

"""
1. merge (sort by start)
2. end-time greedy (pick max non-overlap / min removals)
3. min-heap ends (min rooms)
4. sweep/diff (capacity/max overlap)
"""