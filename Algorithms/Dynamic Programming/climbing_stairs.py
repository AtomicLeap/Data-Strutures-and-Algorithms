# 70. Climbing Stairs

# https://leetcode.com/problems/climbing-stairs/description/

# Recursive solution
def climbing_stairs_r(n: int, memo = {}) -> int:
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n < 0:
        return 0
    steps = [1, 2]
    combination = 0


    for step in steps:
        pos = n - step
        result = climbing_stairs_r(pos, memo)
        combination += result
    memo[n] = combination
    return combination

# m = len(steps)
# n = size of n
# O(m * n) Time complexity
# O(n) Space complexity -> max stack depth of n

# Iterative solution (Tabulation)
def climbing_stairs_i(n: int) -> int:
    table = [0 for _ in range(n + 1)]
    steps = [1, 2]
    table[0] = 1

    for i in range(n + 1):
        if table[i]:
            for step in steps:
                if i + step < n + 1:
                    table[i + step] += table[i]
    return table[n]

# m = len(steps)
# n = size of n
# O(n * m) Time complexity
# O(n) Space complexity => size of the table

# Idea
# This is a Dynamic Programming (DP) problem — similar to the Fibonacci sequence.
# Let’s define:
# f(n)=f(n−1) + f(n−2)
# with base cases:
# f(1) = 1,f(2) = 2

def climbing_stairs_d(n: int, memo = {}) -> int:
    if n in memo:
        return memo[n]
    if n < 3:
        return n
    memo[n] = climbing_stairs_d(n - 1, memo) + climbing_stairs_d(n - 2, memo)
    return memo[n]

# O(n) Time complexity = > memoization with dictionary
# O(n) Space complexity => max stack depth of n

print(climbing_stairs_r(1))
print(climbing_stairs_r(2))
print(climbing_stairs_r(3))
print(climbing_stairs_r(18))
print(climbing_stairs_r(218))

print(climbing_stairs_i(1))
print(climbing_stairs_i(2))
print(climbing_stairs_i(3))
print(climbing_stairs_i(18))
print(climbing_stairs_i(218))

print(climbing_stairs_d(1))
print(climbing_stairs_d(2))
print(climbing_stairs_d(3))
print(climbing_stairs_d(18))
print(climbing_stairs_d(218))