# Leetcode 3600. Maximize Spanning Tree Stability with Upgrades

# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/description/

# Tags -> Binary Search, Greedy, Union-Find, Graph Theory, Minimum Spanning Tree

class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        self.count -= 1
        return True


def max_stability(n: int, edges: list[list[int]], k: int) -> int:
    def check(limit: int) -> bool:
        uf = UnionFind(n)
        for u, v, s, _ in edges:
            if s >= limit:
                uf.union(u, v)
        rem = k
        for u, v, s, _ in edges:
            if s * 2 >= limit and rem > 0:
                if uf.union(u, v):
                    rem -= 1
        return uf.count == 1

    uf = UnionFind(n)
    mn = 10**6
    for u, v, s, must in edges:
        if must:
            mn = min(mn, s)
            if not uf.union(u, v):
                return -1
    for u, v, _, _ in edges:
        uf.union(u, v)
    if uf.count > 1:
        return -1
    l, r = 1, mn
    while l < r:
        mid = (l + r + 1) >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l

print(max_stability(3, [[0,1,2,1],[1,2,3,0]], 1)) # 2
print(max_stability(3, [[0,1,4,0],[1,2,3,0],[0,2,1,0]], 2)) # 6
print(max_stability(3, [[0,1,1,1],[1,2,1,1],[2,0,1,1]], 0)) # -1
