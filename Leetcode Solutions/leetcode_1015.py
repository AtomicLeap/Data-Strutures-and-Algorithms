# Leetcode 1015. Smallest Integer Divisible by K

# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/

# Tag -> Math

# Idea -> Use modular arithmetic. Never build the actual number.
"""
Let:

R1 = 1
R2 = 11
R3 = 111
...
Rn = number made of n ones

We only care about Rn % k.

If we know the remainder of the current repunit, then appending another 1 gives:
R(n+1) = Rn * 10 + 1
R(n+1) % k = (Rn * 10 + 1) % k

We keep generating remainders until one becomes 0. The first time that happens, its length is the answer.
"""

def smallest_repunit_div_by_k(k: int) -> int:
    if k % 2 == 0 or k % 5 == 0:
        return -1

    remainder = 0

    for length in range(1, k + 1):
        remainder = (remainder * 10 + 1) % k

        if remainder == 0:
            return length

    return -1

# O(k) Time complexity, where k is the input number
# O(1) Space complexity

print(smallest_repunit_div_by_k(1)) # 1
print(smallest_repunit_div_by_k(2)) # -1
print(smallest_repunit_div_by_k(3)) # 3
print(smallest_repunit_div_by_k(4)) # -1
print(smallest_repunit_div_by_k(5)) # -1
print(smallest_repunit_div_by_k(6)) # -1
print(smallest_repunit_div_by_k(7)) # 6
print(smallest_repunit_div_by_k(8)) # -1
print(smallest_repunit_div_by_k(9)) # 9
print(smallest_repunit_div_by_k(10)) # -1