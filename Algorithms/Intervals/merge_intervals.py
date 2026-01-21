# Leetcode 56. Merge Intervals

# https://leetcode.com/problems/merge-intervals/description/

def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    intervals.sort(key=lambda x: x[0])
    results = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = results[-1]
        if start <= last_end: # there is an overlap - including touching
            new_start = min(last_start, start) # Optional, since intervals sorted already
            new_end = max(last_end, end)
            results[-1] = [new_start, new_end]
        else:
            results.append([start, end])
    return results

# O(n log n) - Time complexity
# O(n) - Space complexity

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]])) # [[1,6],[8,10],[15,18]]
print(merge_intervals([[1,4],[4,5]])) # [[1,5]]
print(merge_intervals([[4,7],[1,4]])) # [[1,7]]
print(merge_intervals([[1,4],[0,0]])) # [[0,0],[1,4]]