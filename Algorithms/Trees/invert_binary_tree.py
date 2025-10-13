# Leetcode 226. Invert Binary Tree

# https://leetcode.com/problems/invert-binary-tree/description/

# Key Idea
# Both recursive and iterative methods rely on the same fundamental idea:
# For every node, swap its children — repeat this until all nodes are processed.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive solution (Depth First Approach)
def invert_tree_r(root: TreeNode | None) -> TreeNode | None:
    # Base case: if tree is empty
    if not root:
        return None
    
    # Swap the left and right child
    root.left, root.right = root.right, root.left
    
    # Recursively invert the subtrees
    invert_tree_r(root.left)
    invert_tree_r(root.right)
    
    return root

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity


# Iterative solution (Breadth First Approach)
from collections import deque
def invert_tree_i(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None
    
    queue = deque([root])

    while queue:
        node = queue.popleft()

        # Swap children
        node.left, node.right = node.right, node.left

        # Add chidren to queue if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity