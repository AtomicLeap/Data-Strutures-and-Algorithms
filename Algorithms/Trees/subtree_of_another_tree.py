# 572. Subtree of Another Tree

# https://leetcode.com/problems/subtree-of-another-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right= right

# Depth First Search Approach
def is_subtree(root: TreeNode, sub_root: TreeNode) -> bool:
    if not sub_root:   # empty tree is always a subtree
        return True
    if not root:      # sub_root non-empty but root empty -> no
        return False

    # If current node matches, try full compare; otherwise search children
    return (root.val == sub_root.val and _same_helper(root, sub_root)) \
            or is_subtree(root.left, sub_root) \
            or is_subtree(root.right, sub_root)


def _same_helper(a: TreeNode, b: TreeNode) -> bool:
    if not a and not b:
        return True
    if not a or not b or a.val != b.val:
        return False
    return _same_helper(a.left, b.left) and _same_helper(a.right, b.right)

# n, m - number of nodes
# O(n.m) - Time complexity
# O(h) where h is the tree height - Space complexity