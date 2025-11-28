# Leetcode 133. Clone Graph

# https://leetcode.com/problems/clone-graph/description/

# Key idea:
"""
Use a hash map (dictionary) to remember the mapping from each original node to its cloned node.
Then run DFS or BFS:

When we first see a node:
1. Create its clone Node(node.val, [])
2. Store old_node -> new_node in the map

For each neighbor:
1. If not cloned yet, recursively/iteratively clone it
2. Append the cloned neighbor to the current cloned node's neighbor list

This guarantees:
1. We don't re-clone the same node
2. Cycles are handled correctly

Complexity: O(V + E) time, O(V) extra space
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# DFS (Recursively)
from typing import Optional, List

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph_dfs(node: 'Optional[Node]') -> 'Optional[Node]':
    if node is None:
        return None

    # Map from original node -> cloned node
    cloned = {}

    def dfs_helper(curr: 'Node') -> 'Node':
        # If already cloned, return the clone
        if curr in cloned:
            return cloned[curr]

        # Create clone of current node (neighbors will be filled later)
        copy = Node(curr.val)
        cloned[curr] = copy

        # Clone all neighbors
        for neighbor in curr.neighbors:
            copy.neighbors.append(dfs_helper(neighbor))

        return copy

    return dfs_helper(node)

# V = number of nodes (vertices)
# E = number of edges
# O(V + E) Time complexity
# O(V) Space complexity

# BFS (Iteratively)

from collections import deque
from typing import Optional, List


def clone_graph_bfs(node: 'Optional[Node]') -> 'Optional[Node]':
    if node is None:
        return None

    # Map original -> clone
    cloned = {node: Node(node.val)}
    queue = deque([node])

    while queue:
        curr = queue.popleft()
        curr_clone = cloned[curr]

        for neighbor in curr.neighbors:
            if neighbor not in cloned:
                cloned[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            curr_clone.neighbors.append(cloned[neighbor])

    return cloned[node]

# V = number of nodes (vertices)
# E = number of edges
# O(V + E) Time complexity
# O(V) Space complexity

print(clone_graph_dfs([[2,4],[1,3],[2,4],[1,3]])) # [[2,4],[1,3],[2,4],[1,3]]
print(clone_graph_dfs([[]])) # [[]]
print(clone_graph_dfs([])) # []

print(clone_graph_bfs([[2,4],[1,3],[2,4],[1,3]])) # [[2,4],[1,3],[2,4],[1,3]]
print(clone_graph_bfs([[]])) # [[]]
print(clone_graph_bfs([])) # []