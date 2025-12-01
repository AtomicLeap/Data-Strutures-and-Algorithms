# Leetcode 261. Graph Valid Tree

# https://leetcode.com/problems/graph-valid-tree/description/

# Idea
"""
You must return True iff these edges form a valid tree.

A graph is a tree iff:

1. It is connected - exactly one connected component.
2. It has no cycles.
3. Equivalently, for n nodes it has exactly n - 1 edges and is connected. 

Key observations

For an undirected graph to be a tree:

1. Edge count check
If len(edges) != n - 1, it cannot be a tree.
If fewer edges → disconnected.
If more edges → must contain a cycle.

2. Connectivity / cycle check
After edge count passes, you only need to check that the graph is connected.
You can do this with:

a. Union-Find (Disjoint Set Union), or
b. DFS/BFS from node 0 and ensure all n nodes are visited.
"""

# Using Union Find
from typing import List

def valid_tree(n: int, edges: List[List[int]]) -> bool:
    # 1. Quick edge-count check
    if len(edges) != n - 1:
        return False

    # 2. Union-Find / Disjoint Set Union (DSU)
    parent = list(range(n))
    rank = [0] * n  # optional optimization

    def find(x: int) -> int:
        # Path compression
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int) -> bool:
        # Returns False if x and y are already connected (cycle)
        root_x, root_y = find(x), find(y)
        if root_x == root_y:
            return False  # cycle detected

        # Union by rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True

    # 3. Process all edges; if any union fails → cycle
    for u, v in edges:
        if not union(u, v):
            return False

    # 4. If we got here, no cycles; with n-1 edges that implies connected
    return True

# O(E . α(n)) ≈ O(E) Time complexity
# O(n) Space complexity


# Using DFS

from typing import List
from collections import defaultdict

def valid_tree_dfs(n: int, edges: List[List[int]]) -> bool:
    # Edge-count condition
    if len(edges) != n - 1:
        return False

    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs_helper(node: int, parent: int) -> bool:
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue  # don't go back on the same edge
            if neighbor in visited:
                return False  # found a cycle
            if not dfs_helper(neighbor, node):
                return False
        return True

    # Start DFS from node 0
    if not dfs_helper(0, -1):
        return False

    # Check connectivity
    return len(visited) == n

# O(n + E) = O(n) Time complexity, since E = n - 1
# O(n) Space complexity

print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])) # True
print(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])) # False

print(valid_tree_dfs(5, [[0, 1], [0, 2], [0, 3], [1, 4]])) # True
print(valid_tree_dfs(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])) # False