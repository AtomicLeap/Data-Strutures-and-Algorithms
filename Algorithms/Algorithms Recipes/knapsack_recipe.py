# 0/1 Knapsack Recipe

"""
Given n items where each item has some weight and value associated 
with it and also given a bag with capacity C, [i.e., the bag can hold 
at most C weight in it]. The task is to put the items into the bag such 
that the sum of values associated with them is the maximum possible.

Note: The constraint here is we can either put an item completely into 
the bag or cannot put it at all [It is not possible to put a part of 
an item into the bag].

Input:  W = 4, value[] = [1, 2, 3], weight[] = [4, 5, 1]
Output: 3

Input: W = 3, value[] = [1, 2, 3], weight[] = [4, 5, 6]
Output: 0
"""

# Use Brute-Force Approach (Recursion)
def knapsack_r(wt: list[int], val: list[int], cap: int) -> int:
    def _k_helper(cap: int, idx: int) -> int:
        if idx == len(wt) or cap == 0:
            return 0
        
        # Not picking the current item
        not_pick = _k_helper(cap, idx + 1)

        # Pick the current item (if it fits)
        pick = 0
        if wt[idx] <= cap:
            pick = val[idx] + _k_helper(cap - wt[idx], idx + 1)
        
        # Return the maximum o the two choices
        return max(pick, not_pick)
    
    return _k_helper(cap, 0)

# O (2 ^ n) - Time complexity
# O (n) = Space-complexity

print(knapsack_r([4, 5, 1], [1, 2, 3], 4)) # 3
print(knapsack_r([4, 5, 6], [1, 2, 3], 3)) # 0

# Use Memoization (Recursion + cache)
def knapsack_m(wt: list[int], val: list[int], cap: int) -> int:
    n = len(wt)
    # Base case
    if n == 0 or cap <= 0:
        return 0
    
    memo = [[-1] * (cap + 1) for _ in range(n)]

    def _k_helper(cap: int, idx: int) -> int:
        # Base case
        if idx == n or cap == 0:
            return 0
        
        # Check if previously calculated same sub-problem
        if memo[idx][cap] != -1:
            return memo[idx][cap]
        
        # Not picking the current item
        not_pick = _k_helper(cap, idx + 1)

        # Pick the current item (if it fits)
        pick = 0
        if wt[idx] <= cap:
            pick = val[idx] + _k_helper(cap - wt[idx], idx + 1)

        memo[idx][cap] = max(pick, not_pick)
        return memo[idx][cap]
    
    return _k_helper(cap, 0)

# n = length of weight, c = capacity
# O (n * c) - Time complexity
# O (n * c) (+ recursion stack) - Space-complexity

print(knapsack_m([4, 5, 1], [1, 2, 3], 4)) # 3
print(knapsack_m([4, 5, 6], [1, 2, 3], 3)) # 0

# Use Tabulation Approach
def knapsack_t(wt: list[int], val: list[int], cap: int) -> int:
    n = len(wt)
    table = [[0] * (cap + 1) for _ in range(n)]

    # Handle the first row first, considering only the first item
    for capacity in range(cap + 1):
        if capacity >= wt[0]:
            table[0][capacity] = val[0]

    # Fill the remaining rows
    for idx in range(1, n):
        for capacity in range(cap + 1):
            not_pick = table[idx - 1][capacity] # Do not pick the current item
            pick = 0
            if wt[idx] <= capacity:
                pick = val[idx] + table[idx - 1][capacity - wt[idx]] # Pick the current item
            table[idx][capacity] = max(pick, not_pick)
    return table[n - 1][cap]

# n = length of weight, c = capacity
# O (n * c) - Time complexity
# O (n * c) - Space-complexity

print(knapsack_t([4, 5, 1], [1, 2, 3], 4)) # 3
print(knapsack_t([4, 5, 6], [1, 2, 3], 3)) # 0