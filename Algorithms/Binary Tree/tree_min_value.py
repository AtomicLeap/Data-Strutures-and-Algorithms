# tree min value

"""
Write a function, tree_min_value, that takes in the root of a binary tree that contains
number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""

import sys

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree_min_value_dfr(root: Node) -> int:
    if not root: return sys.maxsize

    left = tree_min_value_dfr(root.left)
    right = tree_min_value_dfr(root.right)
    return min(root.val, left, right)

def tree_min_value_dfi(root: Node) -> int:
    stack = [root]
    min_val = None

    while stack:
        current = stack.pop()
        if not min_val or min_val and current.val < min_val:
            min_val = current.val

        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return min_val

def tree_min_value_bf(root: Node) -> int:
    queue = [root]
    min_val = None

    while queue:
        current = queue.pop(0)
        if not min_val or min_val and current.val < min_val:
            min_val = current.val
        
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)

    return min_val


a = Node(3)
b = Node(11)
c = Node(4)
d = Node(4)
e = Node(-2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#       3
#    /    \
#   11     4
#  / \      \
# 4   -2     1

a_1= Node(-1)
b_1 = Node(-6)
c_1 = Node(-5)
d_1 = Node(-3)
e_1 = Node(-4)
f_1 = Node(-13)
g_1 = Node(-2)
h_1 = Node(-2)

a_1.left = b_1
a_1.right = c_1
b_1.left = d_1
b_1.right = e_1
c_1.right = f_1
e_1.left = g_1
f_1.right = h_1

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   -4   -13
#     /       \
#    -2       -2

a_2= Node(5)
b_2 = Node(11)
c_2 = Node(3)
d_2 = Node(4)
e_2 = Node(14)
f_2 = Node(12)

a_2.left = b_2
a_2.right = c_2
b_2.left = d_2
b_2.right = e_2
c_2.right = f_2

#       5
#    /    \
#   11     3
#  / \      \
# 4   14     12

a_3 = Node(42)

#        42

print(tree_min_value_dfr(a)) # -> -2
print(tree_min_value_dfr(a_1)) # -> -13
print(tree_min_value_dfr(a_2)) # -> 3
print(tree_min_value_dfr(a_3)) # -> 42
print('---------------------------')
print(tree_min_value_dfi(a)) # -> -2
print(tree_min_value_dfi(a_1)) # -> -13
print(tree_min_value_dfi(a_2)) # -> 3
print(tree_min_value_dfi(a_3)) # -> 42
print('---------------------------')
print(tree_min_value_bf(a)) # -> -2
print(tree_min_value_bf(a_1)) # -> -13
print(tree_min_value_bf(a_2)) # -> 3
print(tree_min_value_bf(a_3)) # -> 42