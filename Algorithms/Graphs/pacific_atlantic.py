# Leetcode 417. Pacific Atlantic Water Flow

# https://leetcode.com/problems/pacific-atlantic-water-flow/description/

from typing import List

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])

    # visited matrices for each ocean
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]

    def dfs_helper(r: int, c: int, visited: List[List[bool]]):
        """Mark all cells reachable from (r, c) moving 'uphill' (height >= current)."""
        
        # directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            # check within bounds of grid
            if 0 <= nr < m and 0 <= nc < n:
                # only continue if:
                # - not yet visited
                # - neighbor is at least as high (so in the real world, water could flow down from neighbor to (r, c))
                if not visited[nr][nc] and heights[nr][nc] >= heights[r][c]:
                    dfs_helper(nr, nc, visited)

    # Start DFS from all Pacific-border cells (top row and left column)
    for c in range(n):
        dfs_helper(0, c, pacific)        # top edge
    for r in range(m):
        dfs_helper(r, 0, pacific)        # left edge

    # Start DFS from all Atlantic-border cells (bottom row and right column)
    for c in range(n):
        dfs_helper(m - 1, c, atlantic)   # bottom edge
    for r in range(m):
        dfs_helper(r, n - 1, atlantic)   # right edge

    # Cells reachable from both oceans
    result = []
    for r in range(m):
        for c in range(n):
            if pacific[r][c] and atlantic[r][c]:
                result.append([r, c])

    return result

# O(m . n) - Time complexity
# O(m . n) - Space complexity

print(pacific_atlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(pacific_atlantic([[1]])) # [[0,0]]