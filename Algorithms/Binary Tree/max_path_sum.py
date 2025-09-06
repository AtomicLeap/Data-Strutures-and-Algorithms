# max root to leaf path sum

"""
Write a function, max_path_sum, that takes in the root of a binary tree that contains 
number values. The function should return the maximum sum of any root to leaf path 
within the tree.

You may assume that the input tree is non-empty.
"""
import sys

min_number = -sys.maxsize - 1

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum_dfr(root: Node) -> int:
    if not root: return min_number
    if not root.left and not root.right:
        return root.val

    return root.val + max(max_path_sum_dfr(root.left), max_path_sum_dfr(root.right))
    
def max_path_sum_dfi(root: Node) -> int:
    result = 0
    min_val_node = Node(min_number)
    stack = [[root, min_val_node]]

    while stack:
        left, right = stack.pop()
        current = max(left.val, right.val)

        if not current.left and current.right:
            stack.append([current.right, min_val_node])
        elif current.left and not current.right:
            stack.append([current.left, min_val_node])
        elif current.left and current.right:
            stack.append([current.left, current.right])
    return result
    

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


a_1 = Node(5)
b_1 = Node(11)
c_1 = Node(54)
d_1 = Node(20)
e_1 = Node(15)
f_1 = Node(1)
g_1 = Node(3)

a_1.left = b_1
a_1.right = c_1
b_1.left = d_1
b_1.right = e_1
e_1.left = f_1
e_1.right = g_1

#        5
#     /    \
#    11    54
#  /   \
# 20   15
#      / \
#     1  3

a_2 = Node(-1)
b_2 = Node(-6)
c_2 = Node(-5)
d_2 = Node(-3)
e_2 = Node(0)
f_2 = Node(-13)
g_2 = Node(-1)
h_2 = Node(-2)

a_2.left = b_2
a_2.right = c_2
b_2.left = d_2
b_2.right = e_2
c_2.right = f_2
e_2.left = g_2
f_2.right = h_2

#        -1
#      /   \
#    -6    -5
#   /  \     \
# -3   0    -13
#     /       \
#    -1       -2


a_3 = Node(42)

#        42

print(max_path_sum_dfr(a)) # -> 18
print(max_path_sum_dfr(a_1)) # -> 59
print(max_path_sum_dfr(a_2)) # -> -8
print(max_path_sum_dfr(a_3)) # -> 42
print('---------------------------')
# print(max_path_sum_dfi(a)) # -> 18
# print(max_path_sum_dfi(a_1)) # -> 59
# print(max_path_sum_dfi(a_2)) # -> -8
# # print(max_path_sum_dfi(a_3)) # -> 42
# print('---------------------------')
# print(max_path_sum_bf(a)) # -> 42
# print(max_path_sum_bf(a_1)) # -> -8
# print(max_path_sum_bf(a_2)) # -> 59
# print(max_path_sum_bf(a_3)) # -> 18
