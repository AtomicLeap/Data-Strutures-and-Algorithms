# Breadth First Traversal (Queue)

# Breadth First Traversal -> Implements Queue Data Structure

# Use breadth first approach to print a list containing all values
# of the tree in breadth-first order

"""
Write a function, breadth_first_values, that takes in the root of a binary tree. 
The function should return an array containing all values of the tree in 
breadth-first order.
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_values(root: Node | None) -> list[str]:
    if not root:
        return []
    # collections.deque in Python is a double-ended queue, so it has methods for 
    # adding/removing items efficiently from both ends - (O(1) time)
    queue = deque([root]) # FIFO method
    result = []

    while queue:
        current = queue.popleft()
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

# n = number of nodes
# O(n) Time complexity
# O(n) Space complexity

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

a_1 = Node('a')
b_1 = Node('b')
c_1 = Node('c')
d_1 = Node('d')
e_1= Node('e')
f_1= Node('f')

a_1.left = b_1
b_1.left = c_1
c_1.right = d_1
d_1.right = e_1

#      a
#       \
#        b
#      /
#      c
#      \
#        d
#         \
#         e

a_2 = Node('a')
b_2 = Node('b')
c_2 = Node('c')
d_2 = Node('d')
e_2 = Node('e')
f_2 = Node('f')
g_2 = Node('g')
h_2 = Node('h')

a_2.left = b_2
a_2.right = c_2
b_2.left = d_2
b_2.right = e_2
c_2.right = f_2
e_2.left = g_2
f_2.right = h_2

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f
#    /       \
#   g         h

print(breadth_first_values(a)) #    -> ['a', 'b', 'c', 'd', 'e', 'f']
print(breadth_first_values(a_1)) #    -> ['a', 'b', 'c', 'd', 'e']
print(breadth_first_values(None)) #    -> []
print(breadth_first_values(a_2)) #    -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
