# largest component

# https://structy.net/problems/largest-component

# NOTE: For undirected graphs, You will always need a visited list/set/dict to 
# keep tract of visited nodes. This is to avoid being trapped in infinite loop.

graph_1 = {
  '0': ['8', '1', '5'],
  '1': ['0'],
  '5': ['0', '8'],
  '8': ['0', '5'],
  '2': ['3', '4'],
  '3': ['2', '4'],
  '4': ['3', '2']
}

graph_2 = {
  '1': ['2'],
  '2': ['1','8'],
  '6': ['7'],
  '9': ['8'],
  '7': ['6', '8'],
  '8': ['9', '7', '2']
}

graph_3 = {
  '3': [],
  '4': ['6'],
  '6': ['4', '5', '7', '8'],
  '8': ['6'],
  '7': ['6'],
  '5': ['6'],
  '1': ['2'],
  '2': ['1']
}

graph_4 = {
  '0': ['4','7'],
  '1': [],
  '2': [],
  '3': ['6'],
  '4': ['0'],
  '6': ['3'],
  '7': ['0'],
  '8': []
}

def largest_component_bf(graph: dict[str, list[str]]) -> int:
    highest_count = 0
    visited = {}

    for node in graph:
        count = _bf_helper(graph, node, visited)
        highest_count = max(highest_count, count)
    return highest_count

def _bf_helper(graph: dict[str, list[str]], node: str, visited: dict[str, int]) -> int:
    queue = [node]
    count = 0

    while queue:
        current = queue.pop(0)

        if current in visited:
            return 0
        
        count += 1
        visited[current] = 1

        for neighbour in graph[current]:
            if neighbour not in queue and neighbour not in visited:
                queue.append(neighbour)
    return count

def largest_component_dfi(graph: dict[str, list[str]]) -> int:
    highest_count = 0
    visited = {}

    for node in graph:
        count = _dfi_helper(graph, node, visited)
        highest_count = max(highest_count, count)
    return highest_count

def _dfi_helper(graph: dict[str, list[str]], node: str, visited: dict[str, int]) -> int:
    stack = [node]
    count = 0

    while stack:
        current = stack.pop()

        if current in visited:
            return 0
        
        count += 1
        visited[current] = 1

        for neighbour in graph[current]:
            if neighbour not in stack and neighbour not in visited:
                stack.append(neighbour)
    return count

def largest_component_dfr(graph: dict[str, list[str]]) -> int:
    highest_count = 0
    visited = {}

    for node in graph:
        count = _dfr_helper(graph, node, visited)
        highest_count = max(highest_count, count)
    return highest_count

def _dfr_helper(graph: dict[str, list[str]], current: str, visited: dict[str, int]) -> int:
    if current in visited:
        return 0
     
    count = 1
    visited[current] = 1
    
    for neighbour in graph[current]:
        count += _dfr_helper(graph, neighbour, visited)
    return count

# e = number of edges
# n = number of nodes
# O(e) Time complexity
# O(n) Space complexity

print(largest_component_bf(graph_1)) # 4
print(largest_component_bf(graph_2)) # 6
print(largest_component_bf(graph_3)) # 5
print(largest_component_bf({})) # 0
print(largest_component_bf(graph_4)) # 3
print('---------------------------------')
print(largest_component_dfi(graph_1)) # 4
print(largest_component_dfi(graph_2)) # 6
print(largest_component_dfi(graph_3)) # 5
print(largest_component_dfi({})) # 0
print(largest_component_dfi(graph_4)) # 3
print('---------------------------------')
print(largest_component_dfr(graph_1)) # 4
print(largest_component_dfr(graph_2)) # 6
print(largest_component_dfr(graph_3)) # 5
print(largest_component_dfr({})) # 0
print(largest_component_dfr(graph_4)) # 3