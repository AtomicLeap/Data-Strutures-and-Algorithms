# Leetcode 263. Ugly Number

# https://leetcode.com/problems/ugly-number/description/

# Tags -> Math

# Idea
"""
Any ugly number can only be built from prime factors 2, 3, and 5.
If after removing all of them something greater than 1 remains, then 
that remainder must contain some other prime factor, so it is not ugly.
"""

def is_ugly(num: int) -> bool:
    if num <= 0:
        return False

    for prime in [2, 3, 5]:
        while num % prime == 0:
            num //= prime

    return num == 1    

# O(log n) Time complexity, where n is the input number
# O(1) Space complexity

print(is_ugly(6)) # True
print(is_ugly(8)) # True    
print(is_ugly(14)) # False
print(is_ugly(1)) # True
print(is_ugly(0)) # False
print(is_ugly(-5)) # False
