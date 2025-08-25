# Queue (FIFO) with list
# Note: Using list pop(0) is O(n)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)     # add at end

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # remove from front
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]     # look at front
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
print(q.dequeue())  # A
print(q.peek())     # B
print(q.size())     # 2
