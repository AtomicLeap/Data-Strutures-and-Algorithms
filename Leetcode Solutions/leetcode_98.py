# Leetcode 98. Validate Binary Search Tree

# https://leetcode.com/problems/validate-binary-search-tree/description/

# Tags -> Binary Tree, Depth-First Search, Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Using DFS
def is_valid_bst(root: TreeNode | None):
    def dfs(node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

    return dfs(root, float("-inf"), float("inf"))

# Using Iterative DFS
def is_valid_bst_i(root: TreeNode | None):
    stack = [(root, float("-inf"), float("inf"))]

    while stack:
        node, low, high = stack.pop()
        if not node:
            continue

        if not (low < node.val < high):
            return False

        stack.append((node.right, node.val, high))
        stack.append((node.left, low, node.val))

    return True

# O(n) - Time complexity
# O(h) - Space complexity