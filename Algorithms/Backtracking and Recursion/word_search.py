# Leetcode 79. Word Search

# https://leetcode.com/problems/word-search/description/

# Using DFS

from collections import Counter

def search_word(board: list[list[str]], word: str) -> bool:
    word_length, m, n = len(word), len(board), len(board[0])

    if word_length > m * n:
        return False
    
    # ----------- Pruning 1: frequency check -----------
    # If the board doesn't contain enough of any character, it's impossible.
    board_counter = Counter(ch for row in board for ch in row)
    word_counter = Counter(word)
    for ch, need in word_counter.items():
        if board_counter[ch] < need:
            return False

    # ----------- Pruning 2: reverse the word if helpful -----------
    # Start from the rarer end of the word to fail faster.
    if board_counter[word[0]] > board_counter[word[-1]]:
        word = word[::-1]

    def dfs_helper(r: int, c: int, idx: int) -> bool:
        if idx == word_length:
            return True
        
        rows_inbound = 0 <= r < m
        cols_inbound = 0 <= c < n

        if not rows_inbound or not cols_inbound:
            return False
        
        if board[r][c] != word[idx]:
            return False

        temp = board[r][c] # Temporary variable to hold value for Backtracking
        board[r][c] = '#' # Marking cell as visited

        # Make recursive calls going down, up, right and left
        result = dfs_helper(r + 1, c, idx + 1) \
                    or dfs_helper(r - 1, c, idx + 1) \
                    or dfs_helper(r, c + 1, idx + 1) \
                    or dfs_helper(r, c - 1, idx + 1)

        if result == True:
            board[r][c] = temp # Recursively Backtrack and fill back cells with original values
            return True
        else:
            board[r][c] = temp # Recursively Backtrack and fill back cells with original values
            return False

    for r in range(m):
        for c in range(n):
            if board[r][c] == word[0] and dfs_helper(r, c, 0):
                return True
            
    return False
    

print(search_word([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")) # True
print(search_word([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")) # True
print(search_word([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")) # False