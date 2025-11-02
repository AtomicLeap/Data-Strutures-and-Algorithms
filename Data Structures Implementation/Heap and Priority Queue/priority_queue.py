# Priority Queue

"""
A Priority Queue is a data structure where each element has a priority. 
Elements with higher priority are served/dequeued before those with lower priority. 
It's commonly used in scheduling algorithms, Dijkstra's shortest path, and more.
"""

# 1. Using heapq (Min-Heap Based)
"""
Python's built-in heapq module provides an efficient way to implement a priority queue 
using a binary heap(min-heap).
"""
import heapq

# Type: (priority, count, item_name)
Entry = tuple[int, str]
h_Entry = tuple[int, int, str]

class PriorityQueue:
    """
    Simple PQ assuming elements are already in tuple form:
      (priority, item_name)
    min priority = highest importance.
    """    
    def __init__(self):
        self.heap: list[h_Entry] = []
        heapq.heapify(self.heap)
        self.count = 0  # To break ties in priority (Handle items with same priority)

    def push(self, entry: Entry) -> None:
        # Lower priority value means higher piority
        priority, item = entry
        _entry: h_Entry = priority, self.count, item
        self.count += 1
        heapq.heappush(self.heap, _entry)

    def pop(self) -> Entry:
        if self.heap:
            priority, _, item = heapq.heappop(self.heap)
            return (priority, item)
        raise IndexError("pop from empty priority queue")

    def peek(self) -> Entry:
        if self.heap:
            priority, _, item = self.heap[0]
            return (priority, item)
        raise IndexError("peek from empty priority queue")

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
    

class MaxPriorityQueue:
    """
    Simple max-priority queue assuming entries already have tuple format:
      (priority, item_name)
    Highest priority value is returned first.
    """
    def __init__(self):
        self._heap: list[h_Entry] = []
        heapq.heapify(self._heap)
        self._count = 0

    def push(self, entry: Entry) -> None:
        priority, item = entry
        _entry: h_Entry = (-priority, self._count, item)
        self._count += 1
        heapq.heappush(self._heap, _entry)

    def pop(self) -> Entry:
        if self._heap:
            priority, _, item = heapq.heappop(self._heap)
            return (-priority, item)
        raise IndexError("pop from empty max priority queue")

    def peek(self) -> Entry:
        if self._heap:
            priority, _, item = self._heap[0]
            return (-priority, item)
        raise IndexError("peek from empty max priority queue")

    def empty(self) -> bool:
        return not self._heap

    def __len__(self) -> int:
        return len(self._heap)  


# 2. Using queue.PriorityQueue (Thread-Safe)

from queue import PriorityQueue as PQ

class ThreadSafePriorityQueue:
    def __init__(self):
        self._pq = PQ()

    def push(self, item, priority):
        self._pq.put((priority, item))

    def pop(self):
        if not self._pq.empty():
            return self._pq.get()
        raise IndexError("pop from empty priority queue")

    def is_empty(self):
        return self._pq.empty()

# O(log n) -> Push, Pop - Time complexity
# O(log n) - Space complexity

