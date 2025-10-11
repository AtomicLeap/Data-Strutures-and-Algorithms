# Leetcode 100. Same Tree

# https://leetcode.com/problems/same-tree/description/

class TreeNode:
    def __init__(self, value= 0, left = None, right = None):
        self.value, self.left, self.right = value, left, right

# Recursive solution (Depth First Approach)
def same_tree_r(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True
    
    if not p or not q or p.value != q.value:
        return False
    
    return same_tree_r(p.left, q.left) and same_tree_r(p.right, q.right)


# Iterative solution (Breadth First Approach)
from collections import deque

def same_tree_i(p: TreeNode | None, q: TreeNode | None) -> bool:
    queue = deque([(p, q)])
    while queue:
        a, b = queue.popleft()
        if not a and not b:
            continue
        if not a or not b or a.val != b.val:
            return False
        queue.append((a.left,  b.left))
        queue.append((a.right, b.right))
    return True
