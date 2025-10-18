# 98. Validate Binary Search Tree

# https://leetcode.com/problems/validate-binary-search-tree/description/

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

# Recursive solution (Depth First Approach)
def _dfs_helper(node, low, high):
    if not node:
        return True
    if not (low < node.val < high):
        return False

    return _dfs_helper(node.left, low, node.val) and _dfs_helper(node.right, node.val, high)
def valid_bst_r(root: TreeNode) -> bool:
    # use infinities to cover full integer range
    return _dfs_helper(root, float("-inf"), float("inf"))

# n - number of nodes
# O(n) - Time complexity
# O(h) recursion stack, h = tree height - Space complexity

# Iterative solution
def valid_bst_i(root: TreeNode) -> bool:
    stack = []
    curr = root
    prev = None  # last visited value in inorder

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev is not None and curr.val <= prev:
            return False
        prev = curr.val
        curr = curr.right
    return True

# n - number of nodes
# O(n) - Time complexity
# O(h) recursion stack, h = tree height - Space complexity