# tree sum

"""
Write a function, tree_sum, that takes in the root of a binary tree that contains number 
values. The function should return the total sum of all values in the tree.
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree_sum_dfr(root: Node | None) -> int:
    if not root: return 0
    return root.val + tree_sum_dfr(root.left) + tree_sum_dfr(root.right)

def tree_sum_dfi(root: Node | None) -> int:
    if not root: return 0
    stack = [root]
    sum_val = 0

    while stack:
        current = stack.pop()
        sum_val += current.val
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return sum_val

def tree_sum_bf(root: Node | None) -> int:
    if not root: return 0
    queue = [root]
    sum_val = 0

    while queue:
        current = queue.pop(0)
        sum_val += current.val
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return sum_val

# n = number of nodes
# O(n) Time complexity
# O(n) Space complexity

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


a_1 = Node(1)
b_1 = Node(6)
c_1 = Node(0)
d_1 = Node(3)
e_1 = Node(-6)
f_1 = Node(2)
g_1 = Node(2)
h_1 = Node(2)

a_1.left = b_1
a_1.right = c_1
b_1.left = d_1
b_1.right = e_1
c_1.right = f_1
e_1.left = g_1
f_1.right = h_1

#      1
#    /   \
#   6     0
#  / \     \
# 3   -6    2
#    /       \
#   2         2

print(tree_sum_dfr(a)) # -> 21
print(tree_sum_dfr(a_1)) # -> 10
print(tree_sum_dfr(None)) # -> 0
print('-------------------------')
print(tree_sum_dfi(a)) # -> 21
print(tree_sum_dfi(a_1)) # -> 10
print(tree_sum_dfi(None)) # -> 0
print('-------------------------')
print(tree_sum_bf(a)) # -> 21
print(tree_sum_bf(a_1)) # -> 10
print(tree_sum_bf(None)) # -> 0