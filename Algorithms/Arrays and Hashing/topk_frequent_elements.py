# Leetcode 347. Top K Frequent Elements

"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
"""


from collections import Counter

# Bucket sort solution
def topk_frequent_elements(nums: list[int], k: int) -> list[int]:
    # 1) Frequency map
    freq = Counter(nums)   # O(n)

    # 2) Buckets: index = frequency, value = list of numbers with that frequency
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]  # frequencies are in [0, 1..n]
    for num, f in freq.items():           # O(U) ⊆ O(n)
        buckets[f].append(num)

    # 3) Gather from highest frequency down
    ans = []
    for f in range(n, 0, -1):             # O(n)
        if buckets[f]:
            ans.extend(buckets[f])
            if len(ans) >= k:
                return ans[:k] # constraints guarantee we return earlier

    return ans  # fallback

# O(n) Time complexity -> (counting + filling buckets + single pass over buckets)
# O(n) Space complexity -> for buckets and frequency map

print(topk_frequent_elements([1,1,1,2,2,3,3,3,3,3], 2)) # [3, 1]
print(topk_frequent_elements([1,1,1,2,2,3], 2)) # [1, 2]
print(topk_frequent_elements([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]


import heapq
from collections import Counter

def topk_frequent_heap(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)                               # O(n)
    # min-heap of size k storing (frequency, num)
    heap = []
    for num, f in freq.items():                        # O(U log k)
        if len(heap) < k:
            heapq.heappush(heap, (f, num))
        else:
            heapq.heappushpop(heap, (f, num))
    return [num for _, num in heap]

# O(n log k) Time complexity
# O(k) Space complexity


print(topk_frequent_heap([1,1,1,2,2,3,3,3,3,3], 2)) # [3, 1]
print(topk_frequent_heap([1,1,1,2,2,3], 2)) # [1, 2]
print(topk_frequent_heap([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]