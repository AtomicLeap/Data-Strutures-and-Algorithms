# Union–Find (Disjoint Set Union)

"""
Union-Find is a data structure that efficiently keeps track of groups of connected items.

It supports only two operations:

1. find(x) → returns the representative (root) of the set that x belongs to

2. union(x, y) → merges (unites) the sets containing x and y

DSU answers questions like:
“Are x and y connected?”
“How many connected components are there?”
“Does adding this edge create a cycle?”
“Which group does this element belong to?”
"""

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank   = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False     # already in the same set → cycle detected

        # union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

# O(α(n)) ≈ O(1) - Time complexity
# O(n) Space complexity
