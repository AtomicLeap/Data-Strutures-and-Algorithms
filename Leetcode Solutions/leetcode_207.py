# Leetcode 207. Course Schedule

# https://leetcode.com/problems/course-schedule/description

# Tags -> Depth-First Search, Breadth-First Search, Graph, Topological Sort

from typing import List
from collections import deque

def canFinish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    # Build graph: b -> a
    for a, b in prerequisites:
        graph[b].append(a)
        indegree[a] += 1

    # Start with all courses having no prerequisites
    queue = deque()
    for course in range(num_courses):
        if indegree[course] == 0:
            queue.append(course)

    taken = 0

    while queue:
        course = queue.popleft()
        taken += 1

        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return taken == num_courses
    
# O(V + E) Time complexity - we visit each course and prerequisite once
# O(V + E) Space complexity - for the graph and indegree arrays

print(canFinish(2, [[1, 0]])) # True
print(canFinish(2, [[1, 0], [0, 1]])) # False
print(canFinish(4, [[1, 0], [2, 1], [3, 2]])) # True