# Leetcode 253. Meeting Rooms II

"""
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of 
days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

def min_days_for_meetings(intervals):
    if not intervals:
        return 0
    events = []
    for start, end in intervals:
        events.append((start, 1))   # start
        events.append((end, -1))  # end

    # Sort by time; on ties, end (-1) comes before start (+1)
    events.sort(key=lambda x: (x[0], x[1]))

    count = total_days = 0
    for _, delta in events:
        count += delta
        total_days = max(total_days, count)
    return total_days


# O(n log n) - Time complexity
# O(n) - Space complexity

print(min_days_for_meetings([(0,40),(5,10),(15,20)]))  # 2
print(min_days_for_meetings([(4,9)]))                  # 1
print(min_days_for_meetings([(5,8),(9,15)]))           # 1
print(min_days_for_meetings([(0,8),(8,10)]))           # 1
print(min_days_for_meetings([]))                       # 0
print(min_days_for_meetings([(0,1),(1,2),(2,3)]))      # 1
print(min_days_for_meetings([(0,10),(2,5),(4,6)]))     # 3
print(min_days_for_meetings([(1,4),(1,4),(1,4)]))      # 3
print(min_days_for_meetings([(1,5),(1,3),(1,2),(1,4)]))      # 4
print(min_days_for_meetings([(0,5),(1,5),(2,5),(3,5)]))      # 4
print(min_days_for_meetings([(0,5),(5,10),(4,6)]))      # 2
print(min_days_for_meetings([(0,1_000_000),(1,2),(2,3),(999_999,1_000_000)]))      # 2
print(min_days_for_meetings([(0,10),(2,8),(3,7),(4,6)]))      # 4
print(min_days_for_meetings([(0,2),(2,4),(4,6),(1,3),(3,5)]))      # 2
print(min_days_for_meetings([(0,1),(0,2),(1,2)]))      # 2