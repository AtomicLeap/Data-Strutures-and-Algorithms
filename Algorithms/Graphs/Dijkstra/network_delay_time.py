# Leetcode 743. Network Delay Time

# https://leetcode.com/problems/network-delay-time/description/

# Key Idea
"""
This is a single-source shortest paths problem on a directed weighted graph 
with non-negative edge weights, so the right tool is Dijkstra's algorithm.
We send the signal from k. The time for all nodes to receive it is the 
maximum among the shortest times from k to every node. If any node is 
unreachable, return -1. Thus:

1. Build adjacency list: u -> (v, w)
2. Run Dijkstra from k to compute dist[1..n]
3. Answer = max(dist) if all finite else -1
"""

from typing import List
import heapq
import math

# 1. Use Dijkstra Algorithm - Best solution
def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    # Build graph
    graph = [[] for _ in range(n + 1)]
    for u, v, w in times:
        graph[u].append((v, w))

    # Dijkstra
    dist = [math.inf] * (n + 1)
    dist[k] = 0
    priority_queue = [(0, k)] # (current_distance, node)

    while priority_queue:
        distance, node = heapq.heappop(priority_queue)
        if distance != dist[node]:
            continue  # stale entry

        for v, w in graph[node]:
            new_distance = distance + w
            if new_distance < dist[v]:
                dist[v] = new_distance
                heapq.heappush(priority_queue, (new_distance, v))

    result = max(dist[1:])  # ignore index 0
    return -1 if result == math.inf else result

# m = len(times), n = number of nodes (vertices)
# O((n + m) log n) - Time complexity
# O(n) - Space complexity

print(network_delay_time([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) # 2
print(network_delay_time([[1,2,1]], n = 2, k = 1)) # 1
print(network_delay_time([[1,2,1]], n = 2, k = 2)) # -1


#2. Use Bellman-Ford Algorithm
def network_delay_time_b(times: List[List[int]], n: int, k: int) -> int:
        # dist[i] = shortest time from k to i
        dist = [math.inf] * (n + 1)
        dist[k] = 0

        # Relax all edges up to (n - 1) times
        for _ in range(n - 1):
            changed = False
            for u, v, w in times:
                if dist[u] != math.inf and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    changed = True
            if not changed:  # early stop if no update in this pass
                break

        result = max(dist[1:])
        return -1 if result == math.inf else result

# m = len(times), n = number of nodes (vertices)
# O(n . m) - Time complexity
# O(n) - Space complexity

print(network_delay_time_b([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)) # 2
print(network_delay_time_b([[1,2,1]], n = 2, k = 1)) # 1
print(network_delay_time_b([[1,2,1]], n = 2, k = 2)) # -1