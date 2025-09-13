# Leetcode 242. Valid Anagram

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your
solution to such a case?
"""

# Unicode-friendly solution:
from collections import Counter

def valid_anagram_c(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# k = number of unique characters.
# O(n) Time complexity
# O(k) Space complexity

print(valid_anagram_c("anagram", "nagaram")) # True
print(valid_anagram_c("rat", "car")) # False
print(valid_anagram_c("racecar", "carrace")) # True
print(valid_anagram_c("jar", "jam")) # False

# Unicode-friendly solution:
def valid_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    word_dict = {}
    for char in s:
        if char not in word_dict:
            word_dict[char] = 1
        else:
            word_dict[char] += 1
    

    for char in t:
        if char not in word_dict or word_dict[char] < 0:
            return False
        word_dict[char] -= 1
    return True

# k = number of unique characters.
# O(n) Time complexity
# O(k) Space complexity

print(valid_anagram("anagram", "nagaram")) # True
print(valid_anagram("rat", "car")) # False
print(valid_anagram("racecar", "carrace")) # True
print(valid_anagram("jar", "jam")) # False

# Not Unicode-friendly solution:
# Use of frequency arrays
def valid_anagram_f(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    # Frequency arrays for 26 lowercase letters
    count = [0] * 26
    
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    # If all counts return to zero, it's an anagram
    return all(x == 0 for x in count)

# n = length of string
# O(n) Time complexity
# O(1) Space complexity -> (fixed 26-length array)

print(valid_anagram_f("anagram", "nagaram")) # True
print(valid_anagram_f("rat", "car")) # False
print(valid_anagram_f("racecar", "carrace")) # True
print(valid_anagram_f("jar", "jam")) # False