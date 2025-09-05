# tree includes

"""
Write a function, treeIncludes, that takes in the root of a binary tree and a 
target targetue. The function should return a boolean indicating whether or not 
the targetue is contained in the tree.
"""
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def tree_includes_dfr(root: Node | None, target) -> bool:
    if not root:
        return False
    if root.val == target:
        return True
    if tree_includes_dfr(root.left, target) == True:
        return True
    if tree_includes_dfr(root.right, target) == True:
        return True
    return False

def tree_includes_dfi(root: Node | None, target) -> bool:
    if not root:
        return False
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val == target:
            return True
        if current.left: stack.append(current.left)
        if current.right: stack.append(current.right)
    return False

def tree_includes_bf(root: Node | None, target) -> bool:
    if not root:
        return False
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current.val == target:
            return True
        if current.left: queue.append(current.left)
        if current.right: queue.append(current.right)
    return False

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

print(tree_includes_dfr(a, "e"))
print(tree_includes_dfr(a_1, "f"))
print(tree_includes_dfr(a_2, "g"))
print(tree_includes_dfr(None, "b"))
print('-------------------------')
print(tree_includes_dfi(a, "e"))
print(tree_includes_dfi(a_1, "f"))
print(tree_includes_dfi(a_2, "g"))
print(tree_includes_dfi(None, "b"))
print('-------------------------')
print(tree_includes_bf(a, "e"))
print(tree_includes_bf(a_1, "f"))
print(tree_includes_bf(a_2, "g"))
print(tree_includes_bf(None, "b"))