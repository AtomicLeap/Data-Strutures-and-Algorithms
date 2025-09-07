# Depth First Traversal (Stack)

# Depth First Traversal -> Implements Stack Data Structure

# Use depth first approach to print all elements of an adjacency list

graph: dict[str, list[str]] = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

# Iteractive method - i
def depth_first_printi(adjacency_list: dict[str, list[str]], source_node: str):
    stack = [ source_node ]

    while stack:
        current = stack.pop()
        print(current)

        for neighbour in adjacency_list[current]:
            stack.append(neighbour)

# Recursive method - r
def depth_first_printr(adjacency_list: dict[str, list[str]], source_node: str):
    print(source_node)
    for neighbour in adjacency_list[source_node]:
        depth_first_printr(adjacency_list, neighbour)

# n = number of nodes
# O(n) Time complexity
# O(n) Space complexity 

depth_first_printi(graph, "a") # acebdf
depth_first_printr(graph, "a") # abdfce
