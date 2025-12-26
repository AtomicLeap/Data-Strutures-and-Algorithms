# Backtracking Recipe

# 1. What is Backtracking?

"""
Backtracking is a systematic search technique for exploring all possible 
solutions to a problem by:

Building a solution incrementally and abandoning (backtracking from) 
partial solutions as soon as they cannot lead to a valid complete solution.

It is essentially DFS (Depth-First Search) on the solution space, with pruning.

Backtracking = DFS + undo + pruning
"""

# 2. When should you think of Backtracking?

"""
Backtracking is appropriate when:

1. The problem asks for all solutions, one valid solution, or count of solutions
2. Choices must be made step by step
3. Constraints can be checked early
4. Brute force is exponential, but pruning helps

Typical keywords:

“generate all”, “find all combinations / permutations”, “valid arrangements”,
“constraint”, “choose / place / assign”
"""

# 3. Intuition (mental model)

"""
Think of solving a maze:

1. Move forward while the path is valid
2. If you hit a dead end → go back
3. Try a different direction

You never explore impossible paths fully.
"""

# 4. Backtracking vs Brute Force

"""
-----------------------------------------------------------------------------
Brute Force	                     |           Backtracking
-----------------------------------------------------------------------------
Explore all possibilities	     |           Prune invalid paths early
Always exponential	             |           Often much faster
No early stopping	             |           Early failure detection

Backtracking is optimized brute force.
"""

# 5. General Backtracking template (VERY IMPORTANT)

"""
Almost every backtracking problem fits this structure:

def backtrack(state):
    if state is a complete solution:
        record solution
        return

    for choice in all possible choices:
        if choice is valid:
            make choice
            backtrack(updated state)
            undo choice   # BACKTRACK


The undo step is what defines backtracking.
"""

# 6. Core components of Backtracking

"""
Every backtracking solution has:

1. State - current partial solution
2. Choices - options at this step
3. Constraints - rules that must hold
4. Goal - complete valid solution
5. Pruning - early rejection
"""

# 7. Classic Backtracking problems

# Example 1: Permutations

"""
def permutation(nums):
    n = len(nums)
    results = []

    def backtrack(combination: list[int], table: list[bool]):
        if len(combination) == n:
            results.append(combination[:])
            return

        for i in range(n):
            if table[i]:
                continue

            table[i] = True
            combination.append(nums[i])

            backtrack(combination, table)

            combination.pop()
            table[i] = False

    backtrack([], [False] * n)
    return results
"""

# Example 2: Subsets

"""
def subsets(nums):
    results = []

    def backtrack(i, combination):
        results.append(combination[:])

        for j in range(i, len(nums)):
            combination.append(nums[j])
            backtrack(j + 1, combination)
            combination.pop()

    backtrack(0, [])
    return results
"""

# Example 3: N-Queens

"""
1. Place queens row by row
2. Check column & diagonal constraints
3. Backtrack on conflict

This is a textbook backtracking problem.
"""

# 8. Backtracking vs Dynamic Programming

"""
----------------------------------------------------------------------------------
Backtracking	                  |              DP
----------------------------------------------------------------------------------
Enumerates solutions	          |              Computes optimal value
Exponential (pruned)	          |              Polynomial
Search-based	                  |              Table-based
Constraint heavy	              |              State transition heavy

Rule:
Need all valid solutions → Backtracking
Need best solution → DP
"""

# 9. Pruning (the key to efficiency)

"""
Pruning means:
Stop exploring a branch as soon as it becomes invalid.

Examples:
-> Duplicate avoidance
-> Sum exceeding target
-> Invalid placements

The better the pruning → the faster the algorithm.
"""

# 10. Backtracking + Optimization

"""
Common enhancements:
-> Sorting input first
-> Using sets / bitmasks
-> Symmetry breaking
-> Constraint propagation
"""

# 11. Common mistakes

"""
-> Forgetting to undo changes
-> Not copying the solution (combination[:])
-> Missing base case
-> Weak pruning
-> Modifying global state incorrectly
"""

# 12. How to recognize a Backtracking problem quickly

"""
Ask yourself:

-> Am I choosing elements step-by-step?
-> Do I need to try multiple possibilities?
-> Can I abandon paths/combinations early?
-> Do I need all solutions or any valid one?

If yes → Backtracking
"""

# 13. Definition (one-liner)

"""
Backtracking is a depth-first search technique that builds solutions incrementally 
and abandons partial solutions as soon as they violate constraints.
"""

# 14. Key insight to remember

"""
Backtracking is DFS + undo + pruning.

That's it.
Backtracking = DFS + undo + pruning
"""

# 15. Final mental checklist

"""
Before writing code:

-> Define the state
-> Define choices
-> Define constraints
-> Define base case
-> Define undo step
"""
