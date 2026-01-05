# Leetcode 57. Insert Interval

# https://leetcode.com/problems/insert-interval/description/

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