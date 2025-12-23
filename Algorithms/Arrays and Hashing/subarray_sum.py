# Leetcode 560. Subarray Sum Equals K

# https://leetcode.com/problems/subarray-sum-equals-k/description/

# Prefix Sum  + Hash Map 

# Idea
"""
Number of subarray sum that equals k ==
count of (prefix_sum - k) in the Hash Map
"""

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_sum = 0
    hash_map = { 0: 1 }
    count = 0

    for num in nums:
        prefix_sum += num
        key = prefix_sum - k
        if key in hash_map:
            count += hash_map[key]
        hash_map[prefix_sum] = hash_map.get(prefix_sum, 0) + 1
    return count

# O(n) Time complexity
# O(n) Space complexity

print(subarray_sum([1, 1, 1], 2)) # 2
print(subarray_sum([1, 2, 3], 3)) # 2
        