# 235. Lowest Common Ancestor of a Binary Search Tree

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


# Iterative solution

# Idea
# Starting at the root:
# If p.val and q.val are both < root.val, the LCA is in the left subtree → go left.
# If both are > root.val, the LCA is in the right subtree → go right.
# Otherwise they split (or one equals the root) → current root is the LCA.
# This works because in a BST all left-subtree values < node, all right-subtree values > node.

def lowest_common_ancestor_i(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    pv, qv = p.val, q.val
    node = root
    while node:
        if pv < node.val and qv < node.val:
            node = node.left            
        elif pv > node.val and qv > node.val:
            node = node.right           
        else:
            return node

# O(h) where h is the tree height - Time complexity
# O(1) - Space complexity

# Recursive solution
def lowest_common_ancestor_r(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor_r(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor_r(root.right, p, q)
    return root

# O(h) where h is the tree height (best O(log n) if balanced, worst O(n) if skewed - Time complexity
# O(h) due to call stack. - Space complexity