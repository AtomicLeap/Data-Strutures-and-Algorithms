# Leetcode 1310. XOR Queries of a Subarray

# https://leetcode.com/problems/xor-queries-of-a-subarray/description/

# Use Prefix_XOR Array (List)
# prefix_xor(l, r) = P[r+1] ^ P[l]

def xor_queries(arr: list[int], queries: list[list[int]]) -> list[int]:
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    results = []

    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    for left, right in queries:
        results.append(prefix_xor[right + 1] ^ prefix_xor[left])
    return results

# O(n) Time complexity
# O(n) Space complexity

print(xor_queries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])) # [2, 7, 14, 8]
print(xor_queries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]])) # [8, 0, 4, 4] 
 