# connected components count

"""
Write a function, connectedComponentsCount, that takes in the adjacency list 
of an undirected graph. The function should return the number of connected 
components within the graph.
"""

graph_1 = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}
graph_2 = {
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}

graph_3 = {
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}

graph_4 = {
  0: [4,7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}

# Assumption used here is that all nodes in a component are unique.
# NOTE: For undirected graphs, You will always need a visited list/set/dict to 
# keep tract of visited nodes. This is to avoid being trapped in infinite loop.

def connected_comp_count__bf(graph: dict[str, list[str]]) -> int:
    count = 0
    visited = {}

    for node in graph:
        if _bf_helper(graph, node, visited) == True:
            count += 1
    return count


def _bf_helper(graph: dict[str, list[str]], node: str, visited: dict[str, int]) -> bool:
    queue = [node]

    while queue:
        current = queue.pop(0)
        
        if current in visited:
            return False
        
        visited[current] = 1

        for neighbour in graph[current]:
            if neighbour not in queue and neighbour not in visited:
                queue.append(neighbour)
    return True

def connected_comp_count__dfi(graph: dict[str, list[str]]) -> int:
    count = 0
    visited = {}

    for node in graph:
        if _dfi_helper(graph, node, visited) == True:
            count += 1
    return count


def _dfi_helper(graph: dict[str, list[str]], node: str, visited: dict[str, int]) -> bool:
    stack = [node]

    while stack:
        current = stack.pop()
        
        if current in visited:
            return False
        
        visited[current] = 1

        for neighbour in graph[current]:
            if neighbour not in stack and neighbour not in visited:
                stack.append(neighbour)
    return True
def connected_comp_count__dfr(graph: dict[str, list[str]]) -> int:
    count = 0
    visited = {}

    for node in graph:
        if _dfr_helper(graph, node, visited) == True:
            count += 1
    return count

def _dfr_helper(graph: dict[str, list[str]], current: str, visited: dict[str, int]) -> bool:
    if current in visited:
        return False
    visited[current] = 1
    for neighbour in graph[current]:
        _dfr_helper(graph, neighbour, visited)
    return True


# e = number of edges
# n = number of nodes
# O(e) Time complexity
# O(n) Space complexity

print(connected_comp_count__bf(graph_1)) # 2
print(connected_comp_count__bf(graph_2)) # 1
print(connected_comp_count__bf(graph_3)) # 3
print(connected_comp_count__bf({})) # 0
print(connected_comp_count__bf(graph_4)) # 5
print('------------------------------------')
print(connected_comp_count__dfi(graph_1)) # 2
print(connected_comp_count__dfi(graph_2)) # 1
print(connected_comp_count__dfi(graph_3)) # 3
print(connected_comp_count__dfi({})) # 0
print(connected_comp_count__dfi(graph_4)) # 5
print('------------------------------------')
print(connected_comp_count__dfr(graph_1)) # 2
print(connected_comp_count__dfr(graph_2)) # 1
print(connected_comp_count__dfr(graph_3)) # 3
print(connected_comp_count__dfr({})) # 0
print(connected_comp_count__dfr(graph_4)) # 5