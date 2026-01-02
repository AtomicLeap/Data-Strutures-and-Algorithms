# Leetcode 278. First Bad Version

# https://leetcode.com/problems/first-bad-version/description/

# Idea
"""
Because versions are monotonic (good → good … → good → bad … → bad), 
the first bad version is the first true in a boolean-sorted array. 
The optimal way to minimize API calls is binary search: O(log n) calls.
"""

# Key idea
"""
Maintain an invariant:
low = smallest candidate index that could be first bad
high = largest candidate index that could be first bad

On each step:
-> Check mid
If isBadVersion(mid) is true, the first bad is at mid or to the left → hi = mid
Else it's to the right → lo = mid + 1

-> Stop when lo == hi → that index is the first bad version.
"""

def first_bad_version(n: int) -> int:
    low, high = 1, n
    while low < high:
        mid = low + (high - low) // 2  # avoids overflow in some languages
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low

# O(log n) - Time complexity
# O(1) - Space complexity


print(first_bad_version(5)) # 4
print(first_bad_version(1)) # 1
