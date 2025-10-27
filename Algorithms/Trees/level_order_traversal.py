# Leetcode 102. Binary Tree Level Order Traversal

# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right

# Recursive solution (Depth First Approach)
def _dfs_helper(node: TreeNode | None, depth: int, results: list):
    if not node:
        return
    if depth == len(results):
        results.append([])
    results[depth].append(node.val)
    _dfs_helper(node.left, depth + 1, results)
    _dfs_helper(node.right, depth + 1, results)

def level_order_traversal_r(root: TreeNode) -> list[list[TreeNode]] | list:
    results = []
    _dfs_helper(root, 0, results)
    return results

# n - number of nodes
# O(n) - Time complexity
# O(h) recursion stack, h = tree height (O(n) worst-case, O(log n) balanced) - Space complexity

# Iterative solution (Breadth First Approach)
from collections import deque

def level_order_traversal_i(root: TreeNode) -> list[list[TreeNode]] | list:
    if not root:
        return []
    queue = deque([root])
    results = []

    while queue:
        result = []
        list_len = len(queue)
        for _ in range(list_len):
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        results.append(result)
    return results

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity