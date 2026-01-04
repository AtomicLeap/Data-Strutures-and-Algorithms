# Leetcode 69. Sqrt(x)

# https://leetcode.com/problems/sqrtx/description/

# Idea
"""
1. We need to search for minimal k satisfying condition k^2 > x,
    then k - 1 is the answer to the question. 
2. also set right = x + 1 instead of right = x to deal with special input cases 
    like x = 0 and x = 1.
"""
def sqrt(x: int) -> int:
    left, right = 0, x + 1

    while left < right:
        mid = (left  + right) // 2
        if mid * mid > x:
            right = mid
        else:
            left = mid + 1
    return left - 1 # `left` is the minimum k value, `k - 1` is the answer

# O(log n) - Time complexity
# O(1) - Space complexity

print(sqrt(4)) # 2
print(sqrt(8)) # 2
print(sqrt(9)) # 3
print(sqrt(25)) # 5
