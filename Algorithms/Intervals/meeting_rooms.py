# Leetcode 252. Meeting Rooms

"""
Given an array of meeting time interval objects consisting of start and end times 
[[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all 
meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

def meeting_rooms(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    
    for idx in range(1, len(intervals)):
        if intervals[idx][0] < intervals[idx - 1][1]:
            return False
    return True

# O(n log n) - Time complexity
# O(n) - Space complexity

print(meeting_rooms([(0,30),(5,10),(15,20)]))  # False
print(meeting_rooms([(0,30),(5,10),(15,20)]))  # False
print(meeting_rooms([(5,8),(9,15)]))           # True
print(meeting_rooms([(0,8),(8,10)]))           # True
print(meeting_rooms([]))                       # True