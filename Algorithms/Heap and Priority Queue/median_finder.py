# Leetcode 295. Find Median from Data Stream

# https://leetcode.com/problems/find-median-from-data-stream/description/

# Use Heap

# Idea (two heaps)
"""
We use 2 heaps. Maintain:

1. max-heap [low]: the smaller half of numbers

2. min-heap [high]: the larger half of numbers

3. Maintain a balance between the lengths of low and high heaps
    --> len(low) == len(high) or len(low) == len(high) + 1
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.low = [] # Max-heap
        self.high = [] # Min-heap
        heapq.heapify(self.low)
        heapq.heapify(self.high)

    def add_number(self, num: int) -> None:
        if not self.low or num <= -self.low[0]:
            heapq.heappush(self.low, -num)
        else:
            heapq.heappush(self.high, num)

        # Balancing checks
        if len(self.low) > len(self.high) + 1:
            value = -heapq.heappop(self.low)
            heapq.heappush(self.high, value)
        elif len(self.high) > len(self.low):
            value = heapq.heappop(self.high)
            heapq.heappush(self.low, -value)
    
    def find_median(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0])/2 # float division
        
        return float(-self.low[0])

# O(log n) -> Add_num, O(1) -> find_median - Time complexity
# O(n) - Space complexity

nums = [2, 6, 1, 9, 4, 8]
solution = MedianFinder()
for num in nums:
    solution.add_number(num)
print(solution.find_median())