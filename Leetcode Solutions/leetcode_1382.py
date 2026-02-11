# Leetcode 1382. Balance a Binary Search Tree

# https://leetcode.com/problems/balance-a-binary-search-tree/description

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Key idea
"""
To rebalance a BST without changing its values, the clean trick is:

1. Inorder traverse the BST → you get the values in sorted order.
2. Build a balanced BST from that sorted list by always picking the middle 
   element as root (recursively).

This guarantees the depth difference at each node is ≤ 1 (height-balanced), 
and it remains a BST.

Inorder → sorted array, then sorted array → balanced BST (pick mid recursively).
"""

def balance_bst(root: TreeNode | None) -> TreeNode | None:
        results = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            results.append(node.val)
            inorder(node.right)

        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            node = TreeNode(results[m])
            node.left = build(l, m - 1)
            node.right = build(m + 1, r)
            return node

        inorder(root)
        return build(0, len(results) - 1)