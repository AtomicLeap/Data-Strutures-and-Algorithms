# Leetcode 57. Insert Interval

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
represent the start and the end of the ith interval and intervals is sorted in ascending order by 
starti. You are also given an interval newInterval = [start, end] that represents the start and 
end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti 
and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

def insert_interval(intervals: list[list[int, int]], new_interval: list[int]) -> list[list[int, int]]:
    idx, n = 0, len(intervals)
    start, end = new_interval
    results = []

    # before interval
    while idx < n and intervals[idx][1] < start:
        results.append(intervals[idx])
        idx += 1

    # merge overlapping intervals
    while idx < n and intervals[idx][0] <= end:
        start = min(start, intervals[idx][0])
        end = max(end, intervals[idx][1])
        idx += 1
    results.append([start, end])

    # after interval
    while idx < n and intervals[idx][0] > end:
        results.append(intervals[idx])
        idx += 1
    return results

# O(n) - Time complexity
# O(n) - Space complexity

print(insert_interval([[1,3],[6,9]], [2,5])) # [[1,5],[6,9]]
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])) # [[1,2],[3,10],[12,16]]