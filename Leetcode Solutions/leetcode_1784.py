# Leetcode 1784. Check if Binary String Has at Most One Segment of Ones

# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/description

# Tags -> String

def check_ones_segment(s: str) -> bool:
    return "01" not in s

# n = len(s)
# O(n) Time complexity
# O(1) Space complexity 

print(check_ones_segment("1001")) # False
print(check_ones_segment("110")) # True
