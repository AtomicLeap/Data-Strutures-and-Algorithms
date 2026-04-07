# Leetcode 8. String to Integer (atoi)

# https://leetcode.com/problems/string-to-integer-atoi/description/

# Tags -> String, Simulation


def my_atoi(s: str) -> int:
    n = len(s)
    i = 0

    # 1. Skip whitespace
    while i < n and s[i] == ' ':
        i += 1

    # 2. Handle sign
    sign = 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # 3. Convert digits
    result = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')

        # 4. Overflow check BEFORE update
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN

        result = result * 10 + digit
        i += 1

    return sign * result

# Complexity Analysis
"""
O(n) - Time complexity, where n is the length of the input string.
O(1) - Space complexity, since we are using only a constant amount of space for variables.
"""
print(my_atoi("42"))            # Output: 42
print(my_atoi("   -42"))        # Output: -42
print(my_atoi("4193 with words"))  # Output: 4193
print(my_atoi("words and 987"))  # Output: 0
print(my_atoi("-91283472332"))  # Output: -2147483648 (clamped to INT_MIN)
print(my_atoi("91283472332"))   # Output: 2147483647 (clamped to INT_MAX)
