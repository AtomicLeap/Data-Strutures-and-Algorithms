# Leetcode 347. Top K Frequent Elements

# https://leetcode.com/problems/top-k-frequent-elements/description/


from collections import Counter

# Bucket sort solution
def topk_frequent_elements(nums: list[int], k: int) -> list[int]:
    # 1) Frequency map
    frequencies = Counter(nums)   # O(n)

    # 2) Buckets: index = frequency, value = list of numbers with that frequency
    n = len(nums)
    buckets = [[] for _ in range(n + 1)]  # frequencies are in [0, 1..n]
    for num, freq in frequencies.items():           # O(U) ⊆ O(n)
        buckets[freq].append(num)

    # 3) Gather from highest frequency down
    answer = []
    for f in range(n, 0, -1):             # O(n)
        if buckets[f]:
            answer.extend(buckets[f])
            if len(answer) >= k:
                return answer[:k] # constraints guarantee we return earlier

    return answer  # fallback

# O(n) Time complexity -> (counting + filling buckets + single pass over buckets)
# O(n) Space complexity -> for buckets and frequency map

print(topk_frequent_elements([1,1,1,2,2,3,3,3,3,3], 2)) # [3, 1]
print(topk_frequent_elements([1,1,1,2,2,3], 2)) # [1, 2]
print(topk_frequent_elements([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]


import heapq
from collections import Counter

def topk_frequent_heap(nums: list[int], k: int) -> list[int]:
    frequencies = Counter(nums)                               # O(n)
    # min-heap of size k storing (frequency, num)
    heap = []
    heapq.heapify(heap)
    for num, freq in frequencies.items():                        # O(U log k)
        if len(heap) < k:
            heapq.heappush(heap, (freq, num))
        else:
            heapq.heappushpop(heap, (freq, num))
    return [num for _, num in heap]

# O(n log k) Time complexity
# O(k) Space complexity


print(topk_frequent_heap([1,1,1,2,2,3,3,3,3,3], 2)) # [3, 1]
print(topk_frequent_heap([1,1,1,2,2,3], 2)) # [1, 2]
print(topk_frequent_heap([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]