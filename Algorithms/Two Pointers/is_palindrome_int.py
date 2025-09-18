# Leetcode 9. Palindrome Number

"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:
-231 <= x <= 231 - 1
Follow up: Could you solve it without converting the integer to a string?
"""

# 1) Palindrome check (integer, no strings)
def is_palindrome_int(x: int) -> bool:
    # negatives and numbers ending with 0 (but not 0 itself) can't be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev = 0
    # reverse only half the digits
    while x > rev:
        rev = rev * 10 + (x % 10)   # take last digit
        x //= 10                    # drop last digit                  

    # For odd digit counts, rev has one extra middle digit → drop it with // 10
    return x == rev or x == rev // 10

# n = number of digits in number
# O(n) - Time complexity
# O(1) - Space complexity

print(is_palindrome_int(121)) # True
print(is_palindrome_int(1221)) # True
print(is_palindrome_int(-121)) # False
print(is_palindrome_int(10)) # False