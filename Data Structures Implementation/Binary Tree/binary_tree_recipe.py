# Binary Tree and Binary Search Tree Recipe

# Binary Tree

# Three conditions make a tree a binary tree. These are, A binary tree must have:

# 1. Only one (1) root node.

# 2. At most two (2) children per node.

# 3. Exactly one (1) path between the root and any node.


# Binary Search Tree

# Three conditions make a tree a valid BST. These are defined as follows:

# 1. The left subtree of a node contains only nodes with keys strictly less than the node's key.

# The right subtree of a node contains only nodes with keys strictly greater than the node's key.

# Both the left and right subtrees must also be binary search trees.



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
