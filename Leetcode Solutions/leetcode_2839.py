# Leetcode 2839. Check if Strings Can be Made Equal With Operations I

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/description

# Tags -> String, Greedy

# Idea
"""
We exploit the fact that both strings have a length of 4. 
This means that we can only have 4 permutations of the characters in s2. 
We can check if s1 is equal to any of these permutations. If it is, then 
we can return True. Otherwise, we return False.
"""

def can_be_equal(s1: str, s2: str) -> bool:
    # Since both strings have length of 4. We know they can only have 4 permutations
    a, b, c, d = s2
    return s1 in (s2, c+b+a+d, a+d+c+b, c+d+a+b)

# O(1) Time complexity
# O(1) Space complexity

print(can_be_equal("abcd", "cdab")) # True
print(can_be_equal("abcd", "dacb")) # False

def can_be_equal_m(s1: str, s2: str) -> bool:
    even_match = (
            (s1[0] == s2[0] and s1[2] == s2[2]) or
            (s1[0] == s2[2] and s1[2] == s2[0])
        )
        
    odd_match = (
            (s1[1] == s2[1] and s1[3] == s2[3]) or
            (s1[1] == s2[3] and s1[3] == s2[1])
        )
        
    return even_match and odd_match

# O(1) Time complexity
# O(1) Space complexity

print(can_be_equal_m("abcd", "cdab")) # True
print(can_be_equal_m("abcd", "dacb")) # False

