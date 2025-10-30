# Leetcode 300. Longest Increasing Subsequence

# https://leetcode.com/problems/longest-increasing-subsequence/description/

from bisect import bisect_left
def longest_subsequence_b(nums: list[int]) -> int:
    tail = []

    for num in nums:
        idx = bisect_left(tail, num)
        if idx == len(tail):
            tail.append(num)
        else:
            tail[idx] = num
    return len(tail)

# O(n log n) Time complexity
# O(n) Space complexity

def longest_subsequence_t(nums: list[int]) -> int:
    n = len(nums)
    table = [1] * n   # Every element starts its own subsequence
    
    for i in range(n):             
        for j in range(i):
            if nums[j] < nums[i]:   # Look at all elements before it
                table[i] = max(table[i], table[j] + 1)
    
    return max(table) if n else 0     # The length of the overall longest subsequence

# O(n ^ 2) Time complexity
# O(n) Space complexity

print(longest_subsequence_b([10,9,2,5,3,7,101,18])) # 4
print(longest_subsequence_b([0,1,0,3,2,3])) # 4
print(longest_subsequence_b([7,7,7,7,7,7,7])) # 1

print(longest_subsequence_t([10,9,2,5,3,7,101,18])) # 4
print(longest_subsequence_t([0,1,0,3,2,3])) # 4
print(longest_subsequence_t([7,7,7,7,7,7,7])) # 1
