# Leetcode 212. Word Search II

# https://leetcode.com/problems/word-search-ii/description/

# Trie + DFS with pruning + Backtracking

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class WordSearch:
    def find_word(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        m, n = len(board), len(board[0])

        # Build Trie
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        results = []

        def dfs(r, c, node):
            # Boundary check FIRST
            rows_in_board_in_bound = 0 <= r < m
            cols_in_board_in_bound = 0 <= c < n

            if not rows_in_board_in_bound or not cols_in_board_in_bound:
                return

            char = board[r][c]

            # Already visited or not in children
            if char == '#' or char not in node.children:
                return

            current = node.children[char] # Current Node

            # Found a word
            if current.word:
                results.append(current.word)
                current.word = None  # Avoid duplicates

            # Mark position as visited
            board[r][c] = '#'

            # DFS neighbors
            dfs(r + 1, c, current)
            dfs(r - 1, c, current)
            dfs(r, c + 1, current)
            dfs(r, c - 1, current)

            # Backtrack
            board[r][c] = char

        # Start DFS from each cell
        for row in range(m):
            for col in range(n):
                dfs(row, col, root)

        return results

# M, N = Number of rows, Number of columns in Board 
# W = number of words
# L = max word length
# O(WL + M.N) - Time complexity
# O(WL) - Space complexity


solution = WordSearch()
print(solution.find_word([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
