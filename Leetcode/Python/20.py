# Leetcode 20. Valid Parentheses
# Data structure -> Stack


def solution(s: str) -> bool:
    # Quick fail: empty string or odd-length strings can’t be perfectly paired
    if not s or len(s) % 2: 
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

def solution_1(s: str)-> bool:
    if not s or len(s) % 2:
        return False

    match = { ")": "(", "}": "{", "]": "[" }
    stack = []

    for char in s:
        if char in ")]}":
            if stack[-1] != match[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not len(stack)

print(solution("()")) # True
print(solution("()[]{}")) # True
print(solution("(]")) # False
print(solution("([])")) # True
print(solution("([)]")) # False
print(solution("")) # False