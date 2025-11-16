# Graph has path problem

# https://structy.net/problems/has-path

# Graph is acyclic - No cycle - This helps to prevent infinite loop
graph: dict[str, list[str]] = {
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

# Depth First search Recursively - r
def has_path_dfr(graph: dict[str, list[str]], src: str, dst: str) -> bool:
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path_dfr(graph, neighbour, dst) == True:
            return True
    return False

# Depth First search Iteractively - i
def has_path_dfi(graph: dict[str, list[str]], src: str, dst: str) -> bool:
    stack = [src]

    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbour in graph[current]:
            stack.append(neighbour)
    return False

# Breath First search
def has_path_bf(graph: dict[str, list[str]], src: str, dst: str) -> bool:
    queue = [src]

    while queue:
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False

# e = number of edges
# n = number of nodes
# O(e) Time complexity
# O(n) Space complexity

print(has_path_dfr(graph, 'f', 'k')) # true
print(has_path_dfr(graph, 'f', 'j')) # false
print(has_path_dfr(graph, 'i', 'h')) # true

print(has_path_dfi(graph, 'f', 'k')) # true
print(has_path_dfi(graph, 'f', 'j')) # false
print(has_path_dfi(graph, 'i', 'h')) # true

print(has_path_bf(graph, 'f', 'k')) # true
print(has_path_bf(graph, 'f', 'j')) # false
print(has_path_bf(graph, 'i', 'h')) # true