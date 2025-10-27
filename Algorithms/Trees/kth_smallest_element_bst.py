# Leetcode 230. Kth Smallest Element in a BST

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value, self.left, self.right = value, left, right


# Iterative solution
def kth_smallest(root: TreeNode, k: int) -> int:
    stack = []
    node = root

    while True:
        # Go as left as possible
        while node:
            stack.append(node)
            node = node.left

        # Process the next node in ascending order
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val

        # Then go to the right subtree
        node = node.right

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity

# Morris Inorder solution
def kth_smallest_m(root: TreeNode, k: int) -> int:
    cur = root
    while cur:
        if not cur.left:
            k -= 1
            if k == 0: 
                return cur.val
            cur = cur.right
        else:
            # Find predecessor
            pre = cur.left
            while pre.right and pre.right is not cur:
                pre = pre.right
            if not pre.right:
                pre.right = cur    # thread
                cur = cur.left
            else:
                pre.right = None   # remove thread
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right

# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity