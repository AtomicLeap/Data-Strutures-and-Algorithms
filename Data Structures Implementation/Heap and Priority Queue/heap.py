# Heap

import heapq

# Type: (priority, item_name)
Entry = tuple[int, str]


# -----------------
# Simple Min Heap
# -----------------
class MinHeap:
    def __init__(self, items: list[Entry] = []):
        self._heap: list[Entry] = list(items) if items else []
        heapq.heapify(self._heap)

    def push(self, entry: Entry) -> None:
        heapq.heappush(self._heap, entry)

    def pop(self) -> Entry:
        if not self._heap:
            raise IndexError("pop from empty MinHeap")
        return heapq.heappop(self._heap)

    def peek(self) -> Entry:
        if not self._heap:
            raise IndexError("peek from empty MinHeap")
        return self._heap[0]

    def __len__(self):
        return len(self._heap)

    def empty(self) -> bool:
        return len(self._heap) == 0
