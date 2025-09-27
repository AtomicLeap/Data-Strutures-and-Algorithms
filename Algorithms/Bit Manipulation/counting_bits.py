# Leetcode 338. Counting Bits

"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 
Constraints:
0 <= n <= 105
 
Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in 
linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

# Idea, Use the relation:
# bits[i] = bits[i >> 1] + (i & 1)
# Right-shift drops the least significant bit; (i & 1) adds 1 if i is odd.
def count_bits(n: int):
    ans = [0]*(n+1)
    for i in range(1, n+1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

# O(n) - Time complexity -> where b is the number of bits, still efficient in practice.
# O(n) - Space complexity -> for the output array

def count_bits_alt(n: int):
    ans = [0]*(n+1)
    for i in range(1, n+1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans

# O(n) - Time complexity -> where b is the number of bits, still efficient in practice.
# O(n) - Space complexity -> for the output array

print(count_bits(2)) # [0,1,1]
print(count_bits(2)) # [0,1,1,2,1,2]

print(count_bits_alt(2)) # [0,1,1]
print(count_bits_alt(2)) # [0,1,1,2,1,2]
