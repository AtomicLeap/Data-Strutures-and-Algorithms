# Leetcode 104. Maximum Depth of Binary Tree

# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

# Recursive solution (Depth First Approach)

# Idea:
# The depth of a node = 1 + max(depth of left subtree, depth of right subtree)
def max_depth_r(root: TreeNode | None) -> int:
    if not root:
        return 0

    left_depth = max_depth_r(root.left)
    right_depth = max_depth_r(root.right)
    return 1 + max(left_depth, right_depth)

# Iterative Approach (Breadth First Approach/Level Order Traversal)

# Idea of BFS Solution
# Each iteration of the while loop processes one level of the tree.
# depth increases after each level is processed.

from collections import deque

def max_depth_i(root: TreeNode | None) -> int:
    if not root:
        return 0

    queue = deque([root])
    depth = 0
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth
