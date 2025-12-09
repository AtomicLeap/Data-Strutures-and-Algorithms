# Leetcode 323. Number of Connected Components in an Undirected Graph

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/


# Using Union Find Method
from typing import List

def count_components(n: int, edges: List[List[int]]) -> int:
    # Initially, each node is its own parent (n components)
    parent = list(range(n))
    rank = [0] * n  # or use size instead of rank
    components = n   # start with n separate components

    def find(x: int) -> int:
        """Find with path compression."""
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x: int, y: int) -> int:
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            # already in the same component
            return 0

        # Union by rank: attach smaller tree under larger one
        if rank[root_y] > rank[root_x]:
            parent[root_x] = root_y
            rank[root_y] += rank[root_x]
        else:
            parent[root_y] = root_x
            rank[root_x] += rank[root_y]
        return 1

    # Process all edges
    for u, v in edges:
        components -= union(u, v)

    return components

# O(n + Edges) - Time complexity
# O(n) Space complexity

# Using DFS
from typing import List
from collections import defaultdict

def count_components_dfs(n: int, edges: List[List[int]]) -> int:
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs_helper(node: int) -> None:
        stack = [node]
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)

    components = 0
    for i in range(n):
        if i not in visited:
            components += 1
            dfs_helper(i)

    return components

# O(n + Edges) - Time complexity
# O(n + Edges) Space complexity

print(count_components(3, [[0,1], [0,2]])) # 1
print(count_components(6, [[0,1], [1,2], [2,3], [4,5]])) # 2

print(count_components_dfs(3, [[0,1], [0,2]])) # 1
print(count_components_dfs(6, [[0,1], [1,2], [2,3], [4,5]])) # 2