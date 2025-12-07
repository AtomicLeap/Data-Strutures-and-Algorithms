# Leetcode 207. Course Schedule

# https://leetcode.com/problems/course-schedule/description/

# Idea
"""
Think of this as a cycle detection in a directed graph problem.

Each course = a node
Each prerequisite pair [a, b] = a directed edge b → a (“take b before a”)
You can finish all courses if and only if this graph has no cycle (i.e., it's a DAG (Directed Acyclic Graph)).

A very clean way to check this is using topological sort (Kahn's algorithm).
"""

from collections import deque
from typing import List

def can_finish(num_courses: int, prerequisites: list[list[str]]) -> bool:
    # Build adjacency list and indegree array
    adj = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for a, b in prerequisites:
        # edge: b -> a  (b is a prerequisite of a)
        adj[b].append(a)
        indegree[a] += 1
    
    print(adj, indegree)
    # Queue for all nodes with indegree 0 (no prerequisites)
    q = deque(i for i in range(num_courses) if indegree[i] == 0)

    taken = 0  # count of courses we can finish

    while q:
        course = q.popleft()
        taken += 1

        # "Remove" this course from the graph by updating indegrees
        for neighbor in adj[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    # If we managed to "take" all courses, no cycle exists
    return taken == num_courses

# V = number of nodes (vertices)
# E = number of edges
# O(V + E) Time complexity
# O(V + E) Space complexity

print(can_finish(2, [[1,0]])) # True
print(can_finish(2, [[1,0],[0,1]])) # False
