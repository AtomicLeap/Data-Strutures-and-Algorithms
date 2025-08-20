# Stack (LIFO) with list

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)   # add to top
     
    def pop(self):
        if not self.is_empty():
            return self.items.pop()   # remove from top
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]     # look at top
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())   # 30
print(s.peek())  # 20
print(s.size())  # 2
