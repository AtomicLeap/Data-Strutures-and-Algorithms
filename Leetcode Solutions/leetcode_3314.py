# Leetcode 3314. Construct the Minimum Bitwise Array I

# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/

# Key Idea
"""
Key bit trick
Let x = results[i]. Write x in binary. Suppose x ends with k trailing 1s:

x = .... 0  1 1 1 ... 1
          ^  k ones

When you add 1:
-> those k trailing 1s flip to 0s,
-> the first 0 above them flips to 1.

So x | (x+1) becomes:
-> the higher bits stay the same,
-> the lowest (k+1) bits become all 1s.

That means:
    x | (x+1) = x + 2^k

What this implies for a target p = nums[i]

We want x | (x+1) = p.

From the behavior above, p must end with at least one 1 (i.e., be odd). 
Since nums[i] are primes, the only even prime is 2:

-> If p = 2 → impossible → -1.
-> Otherwise p is odd, and it has some number r ≥ 1 of trailing 1 bits.

Example:
p = 11 = 1011₂ has r = 2 trailing ones.

If p has r trailing ones, then valid k values are:
    k ∈ {0, 1, ..., r - 1}
and the corresponding solution is:
    x= p - 2^k
To minimize x, we subtract the largest power of two possible, i.e. take:
    k = r - 1
So the minimal answer is:
   x = p - 2^(r - 1)

Algorithm
For each prime p:
1. If p == 2, return -1.
2. Count r = number of trailing 1 bits in p.
3. Return p - (1 << (r-1)).

Correctness (why minimal)
-> Any solution corresponds to some k such that p ends with at least (k+1) ones.
-> For each such k, x = p - 2^k works.
-> Bigger k ⇒ bigger 2^k ⇒ smaller x.
-> Maximum feasible k is r-1, so that gives the smallest possible x.
"""

def min_bitwise_array(nums: list[int]) -> list[int]:
    results = []
    for p in nums:
        if p == 2:
            results.append(-1)
            continue

        # count trailing ones in p
        r = 0
        t = p
        while t & 1:
            r += 1
            t >>= 1

        results.append(p - (1 << (r - 1)))
    return results

# O (n log p) ~ O(n) - Time complexity
# O(1) - Space complexity

print(min_bitwise_array([2,3,5,7])) # [-1,1,4,3]
print(min_bitwise_array([11,13,31])) # [9,12,15]
