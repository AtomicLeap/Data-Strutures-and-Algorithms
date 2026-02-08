# Leetcode 110. Balanced Binary Tree

# https://leetcode.com/problems/balanced-binary-tree/description

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    def _dfs_helper(node: TreeNode | None) -> int:
        if not node:
            return 0

        left = _dfs_helper(node.left)
        right = _dfs_helper(node.right)
        if left == -1 or right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    return _dfs_helper(root) != -1

# O(n) - Time complexity
# O(n) - Space complexity
