# Depth First Search + Backtracking Recipe

# Using "Word Search Problem"

# https://leetcode.com/problems/word-search/description/

"""
KEYS: 

In DFS we do 3 PRUNINGS after the Base-case:

1. Check 1 - In-Bounds Check - Check if we are within bounds of Grid
2. Check 2 - Visited Position Check - Check if we already visited(explored)
                the cell (position). This is to prevent being caught in a 
                CYCLE (Infinity Loop). An alternative for this check is 
                using: In-place board marking (board[row][col] = "#")
3. Check 3 - Happy Path Check - If No Happy path exist 
                (Cell char is not character of word)

Backtrack ->

We Backtrack after each recursive search:
 - visited.remove((row, col)) -> Remove Cell from visited
 - OR Alternatively for In-place board marking
    temp = (row, col)
    board[row][col] = "#"
    ...
    board[row][col] = temp

This is to enable subsequent searches to re-use cell

SUMMARY

If Backtracking will be neccessary after DFS (especially in cases 
where count of some aspect of Board is not needed (Island count) 
and every Board cell should be available for exploring):

In-place board marking (board[row][col] = "#") is more Time and Space Efficient
"""

from collections import Counter

# Using a visited Set
def word_search(board: list[list[str]], word: str) -> bool:
    word_length = len(word)
    m = len(board)
    n = len(board[0])

    if word_length > m * n:
        return False

    # OPTIMIZATION Strategies
    board_count = Counter(char for row in board for char in row)
    word_count = Counter(word)

    for char, count in word_count.items():
        if board_count[char] < count:
            return False

    if board_count[word[0]] > board_count[word[-1]]:
        word = word[::-1]

    def dfs_helper(row: int, col: int, visited: set[tuple], idx: int):
        # Base case
        if idx == word_length:
            return True
        
        # PRUNINGS - 3 cases
        # Backtrack - 1 case (Remove Cell from visited)

        rows_inbound = 0 <= row < m
        cols_inbound = 0 <= col < n
        # Check 1, Not within bounds
        if not (rows_inbound and cols_inbound):
            return False
        
        # Check 2, For visited (If char already exist in visited)
        pos = (row, col) # Use tuple because it is immutable data type
        if pos in visited:
            return False

        # Check 3, If No Happy path exist (Not found character of word) 
        char = board[row][col]
        if char != word[idx]:
            return False
        
        visited.add(pos) # Add cell to visisted
        idx += 1 # Increment index/Move to next char in word
        
        results = dfs_helper(row + 1, col, visited, idx) \
            or dfs_helper(row - 1, col, visited, idx) \
            or  dfs_helper(row, col + 1, visited, idx) \
            or dfs_helper(row, col - 1, visited, idx)
        
        visited.remove((row, col)) # Backtrack - To enable subsequent searches to re-use cell
        
        return results
        


    for row in range(m ):
        for col in range(n):
            if board[row][col] == word[0]:
                if dfs_helper(row, col, set(), 0):
                    return True
    return False

print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) #  False
print(word_search([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")) # True

# Using In-place board marking
def word_search_i(board: list[list[str]], word: str) -> bool:
    word_length = len(word)
    m = len(board)
    n = len(board[0])

    if word_length > m * n:
        return False

    # OPTIMIZATION Strategies
    board_count = Counter(char for row in board for char in row)
    word_count = Counter(word)

    for char, count in word_count.items():
        if board_count[char] < count:
            return False

    if board_count[word[0]] > board_count[word[-1]]:
        word = word[::-1]

    def dfs_helper(row: int, col: int, idx: int):
        # Base case
        if idx == word_length:
            return True
        
        # PRUNINGS - 2 cases
        # Backtrack - 1 case

        rows_inbound = 0 <= row < m
        cols_inbound = 0 <= col < n
        # Check 1, Not within bounds
        if not (rows_inbound and cols_inbound):
            return False

        # Check 2, If No Happy path exist (Not found character of word) 
        char = board[row][col]
        if char != word[idx]:
            return False
        

        temp = board[row][col]
        board[row][col] = "#"
        idx += 1 # Increment index/Move to next char in word
        
        results = dfs_helper(row + 1, col, idx) \
            or dfs_helper(row - 1, col, idx) \
            or  dfs_helper(row, col + 1, idx) \
            or dfs_helper(row, col - 1, idx)
        
        board[row][col] = temp # Backtrack - To enable subsequent searches to re-use cell
        
        return results
        


    for row in range(m ):
        for col in range(n):
            if board[row][col] == word[0]:
                if dfs_helper(row, col, 0):
                    return True
    return False

print('------------------------------------------------------------------')
print(word_search_i([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(word_search_i([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(word_search_i([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) #  False
print(word_search_i([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB")) # True