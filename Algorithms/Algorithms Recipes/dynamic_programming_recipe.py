# Dynamic Programming Recipe

# 1. What is Dynamic Programming?

"""
Dynamic Programming is an algorithmic technique for solving complex problems by:
Breaking them into overlapping subproblems, solving each subproblem once, and 
storing its result for reuse.
This avoids redundant computation and converts exponential-time brute force 
into polynomial time.
"""

# 2. When should you think of DP?

"""
A problem is a good candidate for DP if and only if it has both:

1. Optimal Substructure
The optimal solution can be constructed from optimal solutions of its subproblems.

2. Overlapping Subproblems
The same subproblems are solved repeatedly in naive recursion.

If either property is missing → DP is not appropriate.
"""

# 3. Intuition (mental model)

"""
Imagine computing Fibonacci numbers:

fib(5)
├─ fib(4)
│  ├─ fib(3)
│  │  ├─ fib(2)
│  │  └─ fib(1)
│  └─ fib(2)
└─ fib(3)

Notice how fib(3) and fib(2) repeat.

DP says:

“Compute once. Remember forever.”
"""

# 4. Two main styles of DP

# A. Top-Down (Memoization)

"""
1. Recursive
2. Cache results
3. Natural and intuitive

memo = {}

def fib(n):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
"""

# B. Bottom-Up (Tabulation)

"""
1. Iterative
2. Builds from smallest subproblems
3. More memory-efficient

dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
"""

# 5. The DP problem-solving framework (MOST IMPORTANT)

"""
Always follow these steps:

Step 1: Define the state
What does dp[i] or dp[i][j] represent?

Examples:
dp[i] = best answer using first i elements
dp[i][j] = best answer using first i items with capacity j

Step 2: Define the transition
How does the state depend on smaller states?

Example:
dp[i] = min(dp[i−1], dp[i−2]) + cost[i]

Step 3: Base cases
Smallest inputs with known answers.

Step 4: Iteration order
Ensure subproblems are solved before they are needed.

Step 5: Return final state
Usually dp[n] or dp[last][*]
"""

# 6. Classic DP examples

"""
Example 1: Climbing Stairs
dp[i] = dp[i−1] + dp[i−2]

Example 2: 0/1 Knapsack
dp[i][w] = max(
    dp[i−1][w],
    dp[i−1][w − weight[i]] + value[i]
)

Example 3: Longest Common Subsequence (LCS)
dp[i][j] =
    dp[i−1][j−1] + 1    if s1[i−1] == s2[j−1]
    max(dp[i−1][j], dp[i][j−1]) otherwise
"""

# 7. Common DP patterns

"""
----------------------------------------------------------------------------
Pattern	                  |                  Examples
----------------------------------------------------------------------------
1D, DP	                  |                  Fibonacci, House Robber
2D, DP	                  |                  LCS, Edit Distance
Knapsack	              |                  Subset sum, Partition
Interval DP	              |                  Matrix chain multiplication
Bitmask DP	              |                  TSP
DP on Trees	              |                  Tree diameter, coloring
DP on DAGs	              |                  Shortest path
"""

# 8. DP vs Greedy

"""
---------------------------------------------------------------------------
Aspect	           |             DP	                |       Greedy
---------------------------------------------------------------------------
Choices	           |             Global	            |       Local
Backtracking	   |             Yes	            |           No
Guarantees	       |             Always correct	    |       Problem-specific
Complexity	       |             Higher	            |       Lower

If greedy works → prove it.
If unsure → DP.
"""

# 9. Space optimization in DP

"""
Many DP problems only depend on previous states.

Example:

prev2, prev1 = 0, 1
for i in range(2, n+1):
    curr = prev1 + prev2
    prev2 = prev1
    prev1 = curr


Space drops from O(n) to O(1).
"""

# 10. How to recognize a DP problem quickly

"""
Ask yourself:

1. Can I define a state representing partial progress?
2. Does the problem ask for optimal / count / maximum / minimum?
3. Are subproblems reused?

If yes → Dynamic Programming
"""

# 11. Definition (one-liner)

"""
Dynamic Programming solves problems by storing solutions to overlapping 
subproblems and combining them to build an optimal solution efficiently.
"""

# 12. Key insight to remember

"""
DP is not about code — it's about state and transitions.

Once you get those right, implementation is mechanical.
"""
