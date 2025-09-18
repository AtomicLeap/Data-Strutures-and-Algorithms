# Leetcode 125. Valid Palindrome

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

# Without regex
def valid_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare in lowercase
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

# O(n) - Time complexity
# O(1) - Space complexity

# With regex
import re

def valid_palindrome_rp(s: str) -> bool:
    # Keep only alphanumeric characters and make lowercase
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Compare string with its reverse
    
    left, right = 0, len(cleaned_str) - 1

    while left < right:
        if cleaned_str[left] != cleaned_str[right]:
            return False
        left += 1
        right -= 1
    return True

# O(n) - Time complexity
# O(1) - Space complexity

# With regex
import re

def valid_palindrome_r(s: str) -> bool:
    # Keep only alphanumeric characters and make lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Compare string with its reverse
    return cleaned == cleaned[::-1]

# O(n) - Time complexity
# O(n) - Space complexity -> extra space from slicing

print(valid_palindrome("Was it a car or a cat I saw?")) # True
print(valid_palindrome("A man, a plan, a canal: Panama")) # True
print(valid_palindrome("tab a cat")) # False
print(valid_palindrome(" ")) # True

print(valid_palindrome_r("Was it a car or a cat I saw?")) # True
print(valid_palindrome("A man, a plan, a canal: Panama")) # True
print(valid_palindrome_r("tab a cat")) # False
print(valid_palindrome(" ")) # True

print(valid_palindrome_rp("Was it a car or a cat I saw?")) # True
print(valid_palindrome("A man, a plan, a canal: Panama")) # True
print(valid_palindrome_rp("tab a cat")) # False
print(valid_palindrome(" ")) # True