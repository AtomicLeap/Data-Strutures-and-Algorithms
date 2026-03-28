# Leetcode 172. Factorial Trailing Zeroes

# https://leetcode.com/problems/factorial-trailing-zeroes/description/

# Tags -> Math

# Idea: Count the number of 5s in the prime factorization of n!
# Each multiple of 5 contributes at least one 5 to the factorization
# Each multiple of 25 (5^2) contributes an additional 5
# Each multiple of 125 (5^3) contributes another 5, and so on

def trailing_zeroes(n: int) -> int:
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count

# O(log n) - Time complexity
# O(1) - Space complexity

print(trailing_zeroes(3))  # 0
print(trailing_zeroes(5))  # 1
print(trailing_zeroes(0))  # 0
print(trailing_zeroes(25)) # 6
print(trailing_zeroes(100)) # 24
print(trailing_zeroes(1000)) # 249
