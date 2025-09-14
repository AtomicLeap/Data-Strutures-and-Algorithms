# Binary Tree Recipe

# Three conditions that makes a tree, a binary tree are: A binary tree must have:

# 1. Only one (1) root node.

# 2. At most two (2) children per node.

# 3. Exactly one (1) path between the root and any node.


# Binary Tree Node class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

#            a
#          /   \
#         b      c
#       /   \     \
#      d     e     f
