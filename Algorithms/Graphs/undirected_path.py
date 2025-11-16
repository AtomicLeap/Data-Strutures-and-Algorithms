# undirected path problem

# https://structy.net/problems/undirected-path

edges_1 = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]
edges_2 = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
]

def _build_adjacency_list(edges_list: list[list[str]]) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for edge in edges_list:
        [a, b] = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def undirected_path_bf(edges: list[list[str]], node_a: str, node_b: str) -> bool:
    graph = _build_adjacency_list(edges)
    queue = [node_a]
    visited = {}

    while queue:
        current = queue.pop(0)
        visited[current] = 1
        if current == node_b:
            return True
        for neighbour in graph[current]:
            if neighbour not in visited:
                queue.append(neighbour)
    return False

def undirected_path_dfi(edges: list[list[str]], node_a: str, node_b: str) -> bool:
    graph = _build_adjacency_list(edges)
    stack = [node_a]
    visited = {}

    while stack:
        current = stack.pop()
        visited[current] = 1
        if current == node_b:
            return True

        for neighbour in graph[current]:
            if neighbour not in visited:
                stack.append(neighbour)
    return False

def undirected_path_dfr(edges: list[list[str]], node_a: str, node_b: str) -> bool:
    graph = _build_adjacency_list(edges)
    visited = {}
    return _dfr_helper(graph, node_a, node_b, visited)
    
def _dfr_helper(graph: dict[str, list[str]], src: str, dst: str, visited: dict) -> bool:
    if src == dst:
        return True
    if src in visited:
        return False
    
    visited[src] = 1
    
    for neighbour in graph[src]:
        if _dfr_helper(graph, neighbour, dst, visited) == True:
            return True
    return False

# e = number of edges
# n = number of nodes
# O(e) Time complexity
# O(n) Space complexity

print(undirected_path_bf(edges_1, 'j', 'm')) # -> true
print(undirected_path_bf(edges_1, 'm', 'j')) # -> true
print(undirected_path_bf(edges_1, 'l', 'j')) # -> true
print(undirected_path_bf(edges_2, 'k', 'o')) # -> false
print(undirected_path_bf(edges_2, 'i', 'o')) # -> false
print('-----------------------------------------------')
print(undirected_path_dfi(edges_1, 'j', 'm')) # -> true
print(undirected_path_dfi(edges_1, 'm', 'j')) # -> true
print(undirected_path_dfi(edges_1, 'l', 'j')) # -> true
print(undirected_path_dfi(edges_2, 'k', 'o')) # -> false
print(undirected_path_dfi(edges_2, 'i', 'o')) # -> false
print('-----------------------------------------------')
print(undirected_path_dfr(edges_1, 'j', 'm')) # -> true
print(undirected_path_dfr(edges_1, 'm', 'j')) # -> true
print(undirected_path_dfr(edges_1, 'l', 'j')) # -> true
print(undirected_path_dfr(edges_2, 'k', 'o')) # -> false
print(undirected_path_dfr(edges_2, 'i', 'o')) # -> false