# Leetcode 2485. Find the Pivot Integer

# https://leetcode.com/problems/find-the-pivot-integer/description/

# Tags -> Math

# Idea
"""
left = 1 + 2 + ... + x
right = x + (x + 1) + (x + 2) + ... + n

total (Sn) = 1 + 2 + ... + n = n * (n + 1) / 2

Thus:
1 + 2 + ... + x = Sn - x + (x + 1) + (x + 2) + ... + n
x * (x + 1) / 2 = Sn - x * (x - 1) / 2
x^2 = Sn
x = sqrt(Sn)
"""

def pivot_integer(n: int) -> int:
        total = n * (n + 1) // 2
        num = int(total ** 0.5)
        return num if num * num == total else -1

# O(1) Time complexity
# O(1) Space complexity

print(pivot_integer(8)) # 6
print(pivot_integer(1)) # 1
print(pivot_integer(4)) # -1

def pivot_integer_i(n: int) -> int:
    total_sum = n * (n + 1) // 2
    left_sum = 0

    for num in range(1, n + 1):
        left_sum += num
        right_sum = total_sum - left_sum + num

        if left_sum == right_sum:
            return num

    return -1

# O(n) Time complexity, where n is the input integer
# O(1) Space complexity     

print(pivot_integer_i(8)) # 6
print(pivot_integer_i(1)) # 1
print(pivot_integer_i(4)) # -1
