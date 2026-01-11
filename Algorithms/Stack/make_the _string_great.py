# Leetcode 1544. Make The String Great

# https://leetcode.com/problems/make-the-string-great/description/

def make_great_str(s: str) -> str:
    stack = []

    for char in s:
        if stack and stack[-1] != char and stack[-1].lower() == char.lower() :
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

# n = len(s)
# O(n) Time complexity
# O(n) Space complexity 

print(make_great_str("s"))
print(make_great_str("leEeetcode"))
print(make_great_str("abBAcC"))
print(make_great_str(""))

