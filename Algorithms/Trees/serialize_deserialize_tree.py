# Leetcode 297. Serialize and Deserialize Binary Tree

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


# Using Preorder DFS with null markers.

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode | None' = None, right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        results = []
        def dfs_helper(node: TreeNode):
            if not node:
                results.append("#")
                return
            
            results.append(str(node.val))
            dfs_helper(node.left)
            dfs_helper(node.right)

        dfs_helper(root)

        return ','.join(results)

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Turn list into iterator so we can consume values in order
        data_list = iter(data.split(','))

        def dfs_builder():
            value = next(data_list)
            if value == "#": # Use '#' as null marker
                return None
            
            node = TreeNode(int(value))
            node.left = dfs_builder() # Build left subtree
            node.right = dfs_builder() # Build right subtree

            return node

        return dfs_builder()
        

# O(n) - Time complexity
# O(n) - Space complexity