# Leetcode 2976. Minimum Cost to Convert String I

# https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/

# Key Idea
"""
You can model this as a weighted directed graph on 26 letters.
Each rule original[i] -> changed[i] is a directed edge with weight cost[i] 
(keep the minimum cost if duplicates exist).
To convert source[k] to target[k], you're allowed to apply multiple 
operations, i.e. take a path in this graph. So you need the all-pairs 
shortest path between letters, then sum per position.

Because there are only 26 nodes, the fastest/simplest is Floyd-Warshall on a 26x26 matrix.

Algorithm
1. Initialize dist[26][26] = INF, and dist[c][c] = 0.
2. For each rule (u, v, w), set dist[u][v] = min(dist[u][v], w).
3. Run Floyd-Warshall:
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
4. For each index k:
    - let a = source[k], b = target[k]
    - if dist[a][b] is INF → return -1
    - else add it to answer
5. Return total.
"""

def minimum_cost(
    source: str,
    target: str,
    original: list[str],
    changed: list[str],
    cost: list[int]
) -> int:
    INF = 10**18
    ALPHA = 26

    # dist[i][j] = min cost to convert chr(i) -> chr(j)
    dist = [[INF] * ALPHA for _ in range(ALPHA)]
    for i in range(ALPHA):
        dist[i][i] = 0

    # Direct edges (keep cheapest among duplicates)
    for o, c, w in zip(original, changed, cost):
        u = ord(o) - ord('a')
        v = ord(c) - ord('a')
        if w < dist[u][v]:
            dist[u][v] = w

    # Floyd–Warshall for all-pairs shortest paths
    for k in range(ALPHA):
        dk = dist[k]
        for i in range(ALPHA):
            dik = dist[i][k]
            if dik == INF:
                continue
            di = dist[i]
            for j in range(ALPHA):
                nk = dik + dk[j]
                if nk < di[j]:
                    di[j] = nk

    # Sum costs for each position
    results = 0
    for s_ch, t_ch in zip(source, target):
        if s_ch == t_ch:
            continue
        u = ord(s_ch) - ord('a')
        v = ord(t_ch) - ord('a')
        d = dist[u][v]
        if d >= INF:
            return -1
        results += d

    return results

# Complexities
# Floyd-Warshall: 26^3 = 17576 operations -> effectively constant
# Summation over string: O(n)
# Memory: 26^2

print(minimum_cost("abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20])) # 28
print(minimum_cost("aaaa", "bbbb", ["a","c"], ["c","b"], [1, 2])) # 12
print(minimum_cost("abcd", "abce", ["a"], ["e"], [10000])) # -1