# Leetcode 20. Valid Parentheses
# Data structure -> Stack

def valid_parentheses(s: str)-> bool:
    if not s or len(s) % 2:
        return False

    match = { ")": "(", "}": "{", "]": "[" }
    stack = []

    for char in s:
        if char in ")]}":
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack

# n = len(s)
# O(n) Time complexity
# O(n) Space complexity 

def valid_parentheses_alt(s: str) -> bool:
    # Quick fail: empty string or odd-length strings can’t be perfectly paired
    if not s or len(s) & 1:
        return False

    stack = []
    match = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in "([{":
            stack.append(char)
        else:  # ch is a closing bracket
            if not stack or stack[-1] != match[char]:
                return False
            stack.pop()
    return not stack

# n = len(s)
# O(n) Time complexity
# O(n) Space complexity 

print(valid_parentheses("()")) # True
print(valid_parentheses("()[]{}")) # True
print(valid_parentheses("(]")) # False
print(valid_parentheses("([])")) # True
print(valid_parentheses("([)]")) # False
print(valid_parentheses("")) # False