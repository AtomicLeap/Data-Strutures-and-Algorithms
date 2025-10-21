# 105. Construct Binary Tree from Preorder and Inorder Traversal

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive solution using a hash map to avoid array slicing
def build_tree_r(preorder, inorder):
    if not preorder or not inorder:
        return None

    # Map value -> index in inorder for O(1) splits
    idx = {val: i for i, val in enumerate(inorder)}

    # Pointer into preorder to pick roots in order
    pre_i = 0

    def build(in_l, in_r):
        nonlocal pre_i
        if in_l > in_r:
            return None

        # Next root is current preorder element
        root_val = preorder[pre_i]
        pre_i += 1
        root = TreeNode(root_val)

        # Split inorder into left/right parts
        mid = idx[root_val]

        # Build left subtree from inorder[in_l .. mid-1]
        root.left = build(in_l, mid - 1)
        # Build right subtree from inorder[mid+1 .. in_r]
        root.right = build(mid + 1, in_r)
        return root

    return build(0, len(inorder) - 1)

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity

# Iterative solution
def build_tree_i(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    stack = [root]
    in_i = 0

    for p in preorder[1:]:
        node = stack[-1]
        if node.val != inorder[in_i]:
            node.left = TreeNode(p)
            stack.append(node.left)
        else:
            while stack and stack[-1].val == inorder[in_i]:
                node = stack.pop()
                in_i += 1
            node.right = TreeNode(p)
            stack.append(node.right)
    return root

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity