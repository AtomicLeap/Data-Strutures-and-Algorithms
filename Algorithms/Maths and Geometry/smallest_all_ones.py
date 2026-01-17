# Leetcode 3790. Smallest All-Ones Multiple

# https://leetcode.com/problems/smallest-all-ones-multiple/description/

def smallest_all_one(k: int) -> int:
    # impossible if k has factor 2 or 5
    if k % 2 == 0 or k % 5 == 0:
        return -1

    rem = 0
    for length in range(1, k + 1):
        rem = (rem * 10 + 1) % k
        if rem == 0:
            return length

    return -1

# O (k) - Time complexity
# O (1) - Space compexity

# Modulo solution
def smallest_all_one_m(k: int) -> int:
    if k % 2 == 0 or k % 5 == 0:
        return -1

    rem = 1 % k
    length = 1
    visited = set()

    while rem != 0:
        if rem in visited:
            return -1  # cycle detected
        visited.add(rem)

        rem = (rem * 10 + 1) % k
        length += 1

    return length

# O (k) - Time complexity
# O (k) - Space compexity