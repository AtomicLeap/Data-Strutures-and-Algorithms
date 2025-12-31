# Leetcode 202. Happy Number

# https://leetcode.com/problems/happy-number/description/

# This is classic cycle-detection problem.
# Solve using Floyd's Tortoise & Hare (2-Pointer Fast and slow) Algorithm.

def is_happy(n: int) -> bool:
    def next_num(x):
        total = 0
        while x > 0:
            digit = x % 10
            total += digit * digit
            x //= 10
        return total

    slow = n
    fast = next_num(n)

    while fast != 1 and slow != fast:
        slow = next_num(slow)
        fast = next_num(next_num(fast))

    return fast == 1

# O(log n) - Time complexity
# O(1) - Space complexity

# Using a visited Set Method

def is_happy_a(n: int) -> bool:
    visited = set()

    while n != 1 and n not in visited:
        visited.add(n)
        n = sum([int(num) ** 2 for num in str(n)])
    return n == 1

# O(log n) - Time complexity
# O(n) - Space complexity

print(is_happy(19)) # True
print(is_happy(2)) # False
print('--------------------------')
print(is_happy_a(19)) # True
print(is_happy_a(2)) # False