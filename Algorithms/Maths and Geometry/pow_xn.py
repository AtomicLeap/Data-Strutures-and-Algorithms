# 50. Pow(x, n)

# https://leetcode.com/problems/powx-n/description/

# Key Idea: Exponentiation by Squaring

"""
A naïve approach would compute x^n in O(n) time by multiplying repeatedly.
This is too slow when n is large (up to 2^31 - 1)

Instead, we use the identity:

->  x^n -> 1, if n = 0
->  x^n -> (x^(n/2))^2,  if n is even
->  x^n -> x * (x^(n//2))^2, if n is odd

Negative powers are handled by inversion:
->  x^-n = 1/x^n
So if n < 0, compute the positive power and invert the result.

This reduces the problem size by half each time → O(log n) time.
"""

# Recursion solution
def pow(x: float, n: int) -> float:
    def _helper(x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1.0
        
        # Recursive call
        half = _helper(x, n // 2)

        # Combine results
        if n & 1:
            return x * half * half
        return half * half
    
    if n < 0:
        x = 1 / x
        n = -n
    return _helper(x, n)

# O(log n) - Time complexity
# O(1) - Space complexity

print(pow(2.00000, 10)) # 1024.0000
print(pow(2.10000, 3)) # 9.26100
print(pow(2.00000, -2)) # 0.25000


# Iteratice solution
def pow_i(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    
    # when n is negative
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1.0
    while n > 0:
        if n & 1:
            result *= x
        x *= x              # Square base (x)
        n //= 2             # Halve the exponent
    return result

print('-------------------------------')
print(pow_i(2.00000, 10)) # 1024.0000
print(pow_i(2.10000, 3)) # 9.26100
print(pow_i(2.00000, -2)) # 0.25000