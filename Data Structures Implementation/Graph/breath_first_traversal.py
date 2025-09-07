# Breath First Traversal (Queue)

# Breath First Traversal -> Implements Queue Data Structure

# Use breath first approach to print all elements of an adjacency list

graph: dict[str, list[str]] = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}
# Iteractive method (only)
def breath_first_print(adjacency_list: dict[str, list[str]], source_node: str):
    queue = [ source_node ]

    while queue:
        current = queue.pop(0)
        print(current)

        for neighbour in adjacency_list[current]:
            queue.append(neighbour)

# n = number of nodes
# O(n) Time complexity
# O(n) Space complexity

breath_first_print(graph, "a") # abcdef