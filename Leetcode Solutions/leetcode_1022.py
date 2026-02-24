# Leetcode 1022. Sum of Root To Leaf Binary Numbers

# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

# Tags -> Binary Tree, Depth-First Search

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# DFS - Recursive solution
def sum_root_to_leaf_r(root: TreeNode | None) -> int:
    def dfs(node, curr):
        if not node:
            return 0

        curr = (curr << 1) | node.val

        # leaf
        if not node.left and not node.right:
            return curr

        return dfs(node.left, curr) + dfs(node.right, curr)

    return dfs(root, 0)

# O(n) - Time complexity
# O(h) -> Recursive stack(tree height) - Space complexity

# DFS - Iterative solution
def sum_root_to_leaf_i(root: TreeNode | None) -> int:
    if not root:
        return 0

    total = 0
    stack = [(root, 0)]  # (node, value_so_far)

    while stack:
        node, curr = stack.pop()
        curr = (curr << 1) | node.val

        if not node.left and not node.right:
            total += curr
        else:
            if node.right:
                stack.append((node.right, curr))
            if node.left:
                stack.append((node.left, curr))

    return total

# O(n) - Time complexity
# O(n) - Space complexity

print(sum_root_to_leaf_r([1,0,1,0,1,0,1])) # 22
print(sum_root_to_leaf_r([0])) # 0
