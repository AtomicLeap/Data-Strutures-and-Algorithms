# Leetcode 124. Binary Tree Maximum Path Sum

# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeMaxPathSum:
    def max_path_sum(self, root: TreeNode | None) -> int | float:
        self.max_sum = float('-inf')

        def max_path_gain(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            left_gain = max(max_path_gain(node.left), 0)
            right_gain = max(max_path_gain(node.right), 0)

            max_path_through_node = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, max_path_through_node)

            return node.val + max(left_gain, right_gain)

        max_path_gain(root)

        return self.max_sum
    
# O(n) - Time complexity
# O(n) - Worst space complexity, for balanced tree - O(h) -> h = depth of tree