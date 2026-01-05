# Leetcode 435. Non-overlapping Intervals

# https://leetcode.com/problems/non-overlapping-intervals/description/

def remove_overlapping_intervals_k(intervals: list[list[int, int]]) -> int:
    n = len(intervals)
    kept = 0
    intervals.sort(key=lambda x: x[1]) # sort by end time
    last_end = float('-inf')

    for start, end in intervals:
        if start >= last_end: # non-overlapping (touch allowed)
            kept += 1
            last_end = end
    return n - kept

# O(n log n) - Time complexity
# O(1) - Space complexity

def remove_overlapping_intervals_c(intervals: list[list[int, int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    count = 0
    results = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = results[-1]
        if start >= last_end: # non-overlapping (touch allowed)
            results.append([start, end])
        else:
            count += 1
            end = min(last_end, end)
            results[-1] = [last_start, end]
    return count

# O(n log n) - Time complexity
# O(n) - Space complexity

print(remove_overlapping_intervals_k([[1,2],[2,3],[3,4],[1,3]])) # 1
print(remove_overlapping_intervals_k([[1,2],[1,2],[1,2]])) # 2
print(remove_overlapping_intervals_k([[1,2],[2,3]])) # 0 
print(remove_overlapping_intervals_k([[1,100],[11,22],[1,11],[2,12]])) # 2
print('-----------------------------------------------------------')
print(remove_overlapping_intervals_c([[1,2],[2,3],[3,4],[1,3]])) # 1
print(remove_overlapping_intervals_c([[1,2],[1,2],[1,2]])) # 2
print(remove_overlapping_intervals_c([[1,2],[2,3]])) # 0 
print(remove_overlapping_intervals_c([[1,100],[11,22],[1,11],[2,12]])) # 2
