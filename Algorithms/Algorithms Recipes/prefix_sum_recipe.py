# Prefix Sum (Tabulation) Recipe

# 1. What is Prefix Sum?

"""
Prefix Sum is a preprocessing technique that allows you to answer range queries 
efficiently by storing cumulative sums (or other cumulative operations).

Core idea:
Precompute partial results so each query can be answered in O(1) time.
"""

# 2. Intuition (mental model)

"""
Think of a bank account balance:

Each day you add or subtract money

The balance on day i already contains everything from days 0…i

To find the net change from day l to r:

balance[r] - balance[l - 1]


That's exactly prefix sum.
"""

# 3. Formal definition

"""
Given an array:

A = [a0, a1, a2, ..., a(n-1)]

Define prefix sum array:

P[0] = 0
P[i] = a0 + a1 + ... + a(i-1)   for i ≥ 1

So:

P = [0, a0, a0+a1, a0+a1+a2, ...]
"""

# 4. Range sum query (core use)

"""
To get the sum of elements in range [l, r] (inclusive):

sum(l, r) = P[r+1] - P[l]

Example
A = [2, 4, 1, 3, 5]
P = [0, 2, 6, 7, 10, 15]

sum(1, 3) = P[4] - P[1] = 10 - 2 = 8
"""

# 5. Prefix Sum algorithm (basic)

"""
def prefix_sum(arr):
    P = [0]
    for x in arr:
        P.append(P[-1] + x)
    return P

Complexity =>
Preprocessing: O(n)
Each query: O(1)
Space: O(n)
"""

# 6. Prefix Sum vs brute force

"""
---------------------------------------------------
Approach	      |      Time per query
---------------------------------------------------
Brute force	      |      O(n)
Prefix Sum	      |      O(1)

Total for q queries:

Brute force → O(nq)
Prefix Sum → O(n + q)
"""

# 7. Variants of Prefix Sum

# 1. Prefix Product

"""
Used when multiplication is invertible (careful with zeros).

product(l, r) = P[r+1] / P[l]
"""

# 2. Prefix XOR

"""
Used in bitwise problems.

xor(l, r) = P[r+1] ^ P[l]
"""

# 3. Prefix Min / Max

"""
Not invertible → limited use, usually offline.
"""

# 4. Difference Array (reverse prefix sum)

"""
Used for range updates:

diff[l] += x
diff[r+1] -= x


Later recover original array with prefix sum.
"""

# 8. 2D Prefix Sum (very common)

"""
Used in matrix range queries.

Definition
P[i][j] = sum of rectangle (0,0) → (i-1,j-1)

Query rectangle (r1,c1) → (r2,c2)
sum = P[r2+1][c2+1]
    - P[r1][c2+1]
    - P[r2+1][c1]
    + P[r1][c1]


Used in:

-> Image processing
-> Heatmaps
-> Game grids
-> Submatrix problems
"""

# 9. Prefix Sum + Hash Map (advanced)

"""
Used for subarray problems.

Example: Subarray sum equals k

Key idea:
prefix[j] - prefix[i] = k

So:

prefix[i] = prefix[j] - k

Store prefix sums in a hash map.
"""

# 10. When to use Prefix Sum

"""
Use Prefix Sum when:

1. Multiple range queries
2. Query operation is invertible
3. Static data (no frequent updates)
4. You need fast repeated access
"""

# 11. Prefix Sum vs Sliding Window

"""
-----------------------------------------------------------------------------
Prefix Sum	             |           Sliding Window
-----------------------------------------------------------------------------
O(1) query	             |           O(n) single pass
Best for many queries	 |           Best for single optimization
Works offline	         |           Works online
Static data	             |           Dynamic window
"""

# 12. Definition (one-liner)

"""
Prefix Sum is a preprocessing technique that stores cumulative values to answer 
range queries in constant time.
"""

# 13. Key insight to remember (Tabulation)

"""
Prefix Sum (Tabulation) trades memory for speed — compute once, query forever.
"""

# 15. Final checklist

"""
Before using Prefix Sum, ask:

1. Are there multiple range queries?
2. Is the operation invertible?
3. Is the data mostly static?

If yes → Prefix Sum (Tabulation)
"""
