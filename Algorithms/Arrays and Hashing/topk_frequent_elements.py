# Leetcode 347. Top K Frequent Elements

# https://leetcode.com/problems/top-k-frequent-elements/description/


from collections import Counter

# Prefix Frequency Array solution
def topk_frequent_elements(nums: list[int], k: int) -> list[int]:
    # 1) Frequency map
    frequencies = Counter(nums)   # O(n)

    # 2) Prefix Freq. Array: index = frequency, value = list of numbers with that frequency
    n = len(nums)
    prefix_freq = [[] for _ in range(n + 1)]  # frequencies are in [0, 1..n]
    for num, freq in frequencies.items():           # O(U) ⊆ O(n)
        prefix_freq[freq].append(num)

    # 3) Gather from highest frequency down
    results = []
    for idx in range(n, 0, -1):             # O(n)
        if prefix_freq[idx]:
            results.extend(prefix_freq[idx])
            if len(results) >= k:
                return results[:k] # constraints guarantee we return earlier

    return results  # fallback

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

from collections import Counter

def topk_frequent(nums: list[int], k:int) -> list[int]:
    counts = Counter(nums)
    sorted_counts = sorted(((num, freq) for (num, freq) in counts.items()), \
                     key=lambda item: (-item[1], item[0]))
    results = [num for (num, _) in sorted_counts]
    
    return results[:k]

# O(n log n) Time complexity
# O(n) Space complexity

print(topk_frequent([1,1,1,2,2,3,3,3,3,3], 2)) # [3, 1]
print(topk_frequent([1,1,1,2,2,3], 2)) # [1, 2]
print(topk_frequent([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]