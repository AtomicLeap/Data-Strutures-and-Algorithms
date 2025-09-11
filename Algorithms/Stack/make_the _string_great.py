# Make The String Great

# Data structure - Stack

"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and 
remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.
Notice that an empty string is also good.
Input: s = "abBAcC"
Output: ""

Input: s = "leEeetcode"
Output: "leetcode"

Input: s = "s"
Output: "s"
"""

def make_great_str(s: str) -> str:
    if not s:
        return ''
    stack = []

    for i in range(len(s)):
        if stack and stack[-1].lower() == s[i].lower() and stack[-1] != s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return "".join(stack)

# n = len(s)
# O(n) Time complexity
# O(n) Space complexity 

print(make_great_str("s"))
print(make_great_str("leEeetcode"))
print(make_great_str("abBAcC"))
print(make_great_str(""))

