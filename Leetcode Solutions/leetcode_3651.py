# Leetcode 3651. Minimum Cost Path with Teleportations

# https://leetcode.com/problems/minimum-cost-path-with-teleportations/description


# Key Idea
"""
Model this as a shortest-path problem on (k+1) layers:
1. State = (cell, usedTeleports)
2. Normal move (right/down) stays in same layer and costs the destination 
    cell value.
3. Teleport moves from layer t to t+1, costs 0, and can go to any cell 
    with value ≤ current cell value.

Naively, each teleport has too many destinations. We fix that by processing 
teleport destinations in bulk, ordered by cell values.

- Efficient algorithm (Dijkstra + “bulk relax” teleports)

Let N = m*n.
1. Flatten cells into indices id = i*n + j.
2. Create order: all cell ids sorted by gridValue ascending.
3. Run Dijkstra over states (dist, t, id) plus special events:
    - When we pop a node (t, id) with best distance d and t < k,
        we add a teleport-offer event:
        “In layer t+1, all cells with value ≤ grid[id] can be reached 
        with cost d”.
4. To apply a teleport-offer quickly:
    - Find p = upper_bound(values, threshold) - 1 in the sorted-by-value list.
    - Relax all positions 0..p only once per layer using a DSU “next pointer” 
        trick (like skipping processed indices).
    - Each cell position in that sorted list is processed at most once per 
        layer → total bulk teleport work is O(k*N).

Finally, answer is min_t dist[t][target].
"""

# Solution 1

from heapq import heappush, heappop
from bisect import bisect_right

INF = 10**30

def min_cost_with_teleports(grid, k):
    m, n = len(grid), len(grid[0])
    N = m * n

    def idx(i, j): 
        return i * n + j

    # Flatten values
    val = [0] * N
    for i in range(m):
        for j in range(n):
            val[idx(i, j)] = grid[i][j]

    # Cells sorted by value ascending
    order = list(range(N))
    order.sort(key=lambda x: val[x])
    sorted_vals = [val[x] for x in order]

    # dist[t][id]
    dist = [[INF] * N for _ in range(k + 1)]
    start = idx(0, 0)
    target = idx(m - 1, n - 1)
    dist[0][start] = 0

    # DSU "next" arrays per layer for bulk teleport relaxation
    # parent[t][pos] gives next not-yet-processed position in 'order' for layer t
    parent = [list(range(N + 1)) for _ in range(k + 1)]

    def find(t, x):
        # iterative path compression
        while parent[t][x] != x:
            parent[t][x] = parent[t][parent[t][x]]
            x = parent[t][x]
        return x

    def erase(t, x):
        # mark position x processed by linking it to x+1
        parent[t][x] = find(t, x + 1)

    # PQ entries:
    # type 0: node state -> (d, 0, t, id, 0)
    # type 1: teleport offer -> (d, 1, layer, thresholdValue, 0)
    pq = []
    heappush(pq, (0, 0, 0, start, 0))

    while pq:
        d, typ, a, b, _ = heappop(pq)

        if typ == 0:
            t, u = a, b
            if d != dist[t][u]:
                continue

            # Normal moves
            i, j = divmod(u, n)
            if j + 1 < n:
                v = idx(i, j + 1)
                nd = d + val[v]
                if nd < dist[t][v]:
                    dist[t][v] = nd
                    heappush(pq, (nd, 0, t, v, 0))
            if i + 1 < m:
                v = idx(i + 1, j)
                nd = d + val[v]
                if nd < dist[t][v]:
                    dist[t][v] = nd
                    heappush(pq, (nd, 0, t, v, 0))

            # Teleport offer to next layer
            if t < k:
                threshold = val[u]
                # offer applies to layer t+1 at distance d
                heappush(pq, (d, 1, t + 1, threshold, 0))

        else:
            layer, threshold = a, b
            # apply: all cells with value <= threshold in this 'layer' can be reached with cost d
            p = bisect_right(sorted_vals, threshold) - 1
            if p < 0:
                continue

            pos = find(layer, 0)
            while pos <= p:
                cell = order[pos]
                if d < dist[layer][cell]:
                    dist[layer][cell] = d
                    heappush(pq, (d, 0, layer, cell, 0))
                # even if we didn't improve, no later teleport offer (>=d) can help this position
                erase(layer, pos)
                pos = find(layer, pos)

    return min(dist[t][target] for t in range(k + 1))

# O((k.m.n) log (k.m.n)) - Time omplexity
# O(k.m.n) - Space complexity


# Solution 2

def min_cost(grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        points = [(i, j) for i in range(m) for j in range(n)]
        points.sort(key=lambda p: grid[p[0]][p[1]])
        costs = [[float("inf")] * n for _ in range(m)]
        for _ in range(k + 1):
            min_cost = float("inf")
            j = 0
            for i in range(len(points)):
                min_cost = min(min_cost, costs[points[i][0]][points[i][1]])
                if (
                    i + 1 < len(points)
                    and grid[points[i][0]][points[i][1]]
                    == grid[points[i + 1][0]][points[i + 1][1]]
                ):
                    i += 1
                    continue
                for r in range(j, i + 1):
                    costs[points[r][0]][points[r][1]] = min_cost
                j = i + 1
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    if i == m - 1 and j == n - 1:
                        costs[i][j] = 0
                        continue
                    if i != m - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i + 1][j] + grid[i + 1][j]
                        )
                    if j != n - 1:
                        costs[i][j] = min(
                            costs[i][j], costs[i][j + 1] + grid[i][j + 1]
                        )
        return costs[0][0]

# O((k + log m.n)× m.n) - Time omplexity
# O(m.n) - Space omplexity

print(min_cost_with_teleports([[1,3,3],[2,5,4],[4,3,5]], 2)) # 7
print(min_cost_with_teleports([[1,2],[2,3],[3,4]], 1)) # 9
print(min_cost([[1,3,3],[2,5,4],[4,3,5]], 2)) # 7
print(min_cost([[1,2],[2,3],[3,4]], 1)) # 9