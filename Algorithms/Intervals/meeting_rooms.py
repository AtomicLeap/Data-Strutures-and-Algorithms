# Leetcode 252. Meeting Rooms

# https://leetcode.com/problems/meeting-rooms/description/

def meeting_rooms(intervals: list[list[int]])-> bool:
    intervals.sort(key=lambda x: x[0])
    last_end = float('-inf')

    for start, end in intervals:
        if start < last_end:
            return False
        last_end = max(last_end, end)
        
    return True

# O(n log n) - Time complexity
# O(1) - Space complexity

def meeting_rooms_i(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    
    for idx in range(1, len(intervals)):
        if intervals[idx][0] < intervals[idx - 1][1]:
            return False
    return True

# O(n log n) - Time complexity
# O(1) - Space complexity

print(meeting_rooms([(0,30),(5,10),(15,20)]))  # False
print(meeting_rooms([(0,30),(5,10),(15,20)]))  # False
print(meeting_rooms([(5,8),(9,15)]))           # True
print(meeting_rooms([(0,8),(8,10)]))           # True
print(meeting_rooms([]))                       # True
print('----------------------------------------------------')
print(meeting_rooms_i([(0,30),(5,10),(15,20)]))  # False
print(meeting_rooms_i([(0,30),(5,10),(15,20)]))  # False
print(meeting_rooms_i([(5,8),(9,15)]))           # True
print(meeting_rooms_i([(0,8),(8,10)]))           # True
print(meeting_rooms_i([]))                       # True