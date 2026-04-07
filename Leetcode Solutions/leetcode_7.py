# Leetcode 7. Reverse Integer

# https://leetcode.com/problems/reverse-integer/description/

# Tags -> Math

def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31     # -2147483648

    rev = 0

    while x != 0:
        # Extract last digit (handle negatives correctly)
        digit = int(x % 10) if x > 0 else int(x % -10)

        # Remove last digit
        x = (x - digit) // 10

        # Check overflow before multiplication
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
            return 0
        if rev < INT_MIN // 10 or (rev == INT_MIN // 10 and digit < -8):
            return 0

        rev = rev * 10 + digit

    return rev

# Complexity Analysis
"""
O(log|x|) - Time complexity, where |x| is the absolute value of the input integer.
O(1) - Space complexity, since we are using only a constant amount of space for variables.
"""
print(reverse(123))        # Output: 321
print(reverse(-123))       # Output: -321
print(reverse(120))        # Output: 21
print(reverse(0))          # Output: 0
