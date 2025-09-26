# Depth First Traversal (Stack)

# Depth First Traversal -> Implements Stack Data Structure

# Use depth first approach to print a list containing all values
# of the tree in depth-first order

"""
Write a function, depth_first_values, that takes in the root of a binary tree. 
The function should return an array containing all values of the tree in 
depth-first order.
"""

class Node:
    def __init__(self, val):
        self.val =  val
        self.left = None
        self.right = None

# Recursive solution
def depth_first_valuesr(root: Node | None) -> list[str]:
    if root == None:
        return []
 
    left_values = depth_first_valuesr(root.left)
    right_values = depth_first_valuesr(root.right)
    return [root.val] + left_values + right_values

# Iterative solution
def depth_first_valuesi(root: Node | None) -> list[str]:
    if not root:
        return []
    stack = [root] # LIFO method
    result = []

    while stack:
        current = stack.pop()
        result.append(current.val)

        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
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

print(depth_first_valuesr(a)) #    -> ['a', 'b', 'd', 'e', 'c', 'f']
print(depth_first_valuesr(a_1)) #    -> ['a', 'b', 'c', 'd', 'e']
print(depth_first_valuesr(None)) #    -> []
print(depth_first_valuesi(a)) #    -> ['a', 'b', 'd', 'e', 'c', 'f']
print(depth_first_valuesi(a_1)) #    -> ['a', 'b', 'c', 'd', 'e']
print(depth_first_valuesi(None)) #    -> []