# Leetcode 435. Non-overlapping Intervals

"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum 
number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] 
are non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""

def non_overlapping_intervals(intervals: list[list[int, int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    count = 0
    results = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = results[-1]
        if start >= last_end:
            results.append([start, end])
        else:
            count += 1
            end = min(last_end, end)
            results[-1] = [last_start, end]
    return count

# O(n log n) - Time complexity
# O(n) - Space complexity

print(non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]])) # 1
print(non_overlapping_intervals([[1,2],[1,2],[1,2]])) # 2
print(non_overlapping_intervals([[1,2],[2,3]])) # 0 
print(non_overlapping_intervals([[1,100],[11,22],[1,11],[2,12]])) # 2