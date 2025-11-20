# shortest path

# https://structy.net/problems/shortest-path

# NOTE: For undirected graphs, You will always need a visited list/set/dict to 
# keep tract of visited nodes. This is to avoid being trapped in infinite loop.

# The Breath First Approach is best suited for finding Shortest Path between Nodes. 
# Unlike Depth First Approach. BF optimizes the search already!
def shortest_path_bf(edges: list[list[str, str]], node_a, node_b) -> int:
    graph = _build_graph(edges)
    queue = [ [node_a, 0] ]
    visited = {} # prevents visiting already visited nodes -> prevent being caught in Loop
    nodes_track = { node_a: 1 } # prevents appending to queue duplicate neighbour nodes

    while queue:
        current_node = queue.pop(0)
        [current, distance ] = current_node
        nodes_track.pop(current)

        if current == node_b:
            return distance
        
        visited[current] = 1

        for neighbour in graph[current]:
            # Prevent appending neighbours already visited to the queue and prevent appending duplicate niehbours to queue
            if neighbour not in visited and neighbour not in nodes_track:
                queue.append([neighbour, distance + 1])
                nodes_track[neighbour] = 1
    return -1

def _build_graph(edges: list[list[str, str]]) -> dict[str, list[str]]:
    graph = {}

    for edge in edges:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

# e = number of edges
# n = number of nodes
# O(e) Time complexity
# O(n) Space complexity

edges_1 = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
edges_2 = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]
edges_3 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]
edges_4 = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path_bf(edges_1, 'w', 'z')) # -> 2
print(shortest_path_bf(edges_2, 'y', 'x')) # -> 1
print(shortest_path_bf(edges_3, 'a', 'e')) # -> 3
print(shortest_path_bf(edges_4, 'b', 'g')) # -> -1