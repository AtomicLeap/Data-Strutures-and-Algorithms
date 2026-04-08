# Leetcode 130. Surrounded Regions

# https://leetcode.com/problems/surrounded-regions/description

# Tags -> Depth-First Search, Breadth-First Search, Union Find, Matrix


def solve(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    if not board or not board[0]:
        return

    m, n = len(board), len(board[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
            return

        board[r][c] = 'S'  # mark as safe

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # 1. Mark all border-connected O's as safe
    for r in range(m):
        if board[r][0] == 'O':
            dfs(r, 0)
        if board[r][n - 1] == 'O':
            dfs(r, n - 1)

    for c in range(n):
        if board[0][c] == 'O':
            dfs(0, c)
        if board[m - 1][c] == 'O':
            dfs(m - 1, c)

    # 2. Capture surrounded regions and restore safe cells
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':
                board[r][c] = 'X'
            elif board[r][c] == 'S':
                board[r][c] = 'O'

# O(m * n) Time complexity - we visit each cell at most once
# O(m * n) Space complexity - in the worst case, the recursion stack could be

solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
solve([["X"]]) # [["X"]]
solve([["O"]]) # [["O"]]
solve([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]) # [["X","O","X"],["O","X","O"],["X","O","X"]]

