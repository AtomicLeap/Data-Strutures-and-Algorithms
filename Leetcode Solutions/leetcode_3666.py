# Leetcode 3666. Minimum Operations to Equalize Binary String

# https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/description/

# Tags -> Math, String, Breadth-First Search, Union-Find, Ordered Set

# Failed! There a bug in code 
# NOTE: To fix
def min_operations(s: str, k: int) -> int:
    n = len(s)
    z = s.count('0')

    if z == 0:
        return 0

    # If you must flip all positions every time
    if k == n:
        # After 1 flip: all ones only if the string was all zeros
        return 1 if z == n else -1

    # Now k < n
    if k % 2 == 0:
        # mk is always even -> z must be even
        if z % 2 == 1:
            return -1
        return (z + k - 1) // k
    else:
        m = (z + k - 1) // k  # ceil(z/k)
        # Need parity(m) == parity(z)
        if (m % 2) != (z % 2):
            m += 1
        return m
    
# O(n) - Time complexity
# O(1) - Space complexity

from collections import deque
from sortedcontainers import SortedSet

# Correct Solution
def min_operations_c(s: str, k: int) -> int:
    n = len(s)
    ts = [SortedSet() for _ in range(2)]
    for i in range(n + 1):
        ts[i % 2].add(i)
    count_zero = s.count('0')
    ts[count_zero % 2].remove(count_zero)
    q = deque([count_zero])
    ans = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == 0:
                return ans
            l = cur + k - 2 * min(cur, k)
            r = cur + k - 2 * max(k - n + cur, 0)
            t = ts[l % 2]
            j = t.bisect_left(l)
            while j < len(t) and t[j] <= r:
                q.append(t[j])
                t.remove(t[j])
        ans += 1
    return -1
    
# O(n.log n) - Time complexity
# O(1) - Space complexity
    
print(min_operations("110", 1)) # 1
print(min_operations("0101", 3)) # 2
print(min_operations("101", 2)) # -1
