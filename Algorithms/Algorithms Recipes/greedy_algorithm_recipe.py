# Greedy Algorithm Recipe

# 1. What is a Greedy Algorithm?

"""
A Greedy Algorithm builds a solution step by step, and at each step it makes the
locally optimal choice, hoping that these local choices lead to a globally 
optimal solution.
"""

# Key idea:

"""
Make the best choice right now, without reconsidering past decisions.
Once a choice is made, it is never undone.
"""

# 2. When does a Greedy algorithm work?

"""
A greedy approach works only if the problem satisfies two fundamental properties:

1. Greedy Choice Property
A globally optimal solution can be reached by making a locally optimal choice 
at each step.

2️. Optimal Substructure
An optimal solution contains optimal solutions to its subproblems.

If either property fails → Greedy fails.
"""

# 3. Mental model (intuition)

"""
Think of greedy algorithms as:

-> Choosing the cheapest, earliest, largest, or smallest option right now
-> Never looking back
-> Trusting the problem structure to guarantee correctness

This is in contrast to:

Dynamic Programming → explores many possibilities

Backtracking → explores all possibilities
"""

# 4. General Greedy algorithm template

"""
1. Sort or prioritize candidates
2. Initialize empty solution
3. Repeat:
      pick the best available option
      if valid:
          include it

The sorting step is usually what enforces correctness.
"""

# 5. Classic Greedy examples

# Example 1: Activity Selection Problem
"""
Problem:
Select the maximum number of non-overlapping activities.

Greedy choice:
Pick the activity that finishes earliest.

activities.sort(key=lambda x: x.end)

last_end = -∞
count = 0

for act in activities:
    if act.start >= last_end:
        count += 1
        last_end = act.end


Why it works:
Choosing the earliest finishing activity leaves the most room for future activities.
"""

# Example 2: Coin Change (Greedy works sometimes)
"""
Coins: {1, 5, 10, 25}
Amount: 63

Greedy choice: Always pick the largest coin ≤ remaining amount.

Works for canonical coin systems (like US coins), but fails for others.

❌ Coins {1, 3, 4}, amount 6
Greedy → 4 + 1 + 1 (3 coins)
Optimal → 3 + 3 (2 coins)

-> Shows greedy is problem-dependent.
"""

# Example 3: Fractional Knapsack
"""
Greedy choice:
Take items with highest value/weight ratio first.

items.sort(key=lambda x: x.value/x.weight, reverse=True)

This works because items are divisible.
"""

# Example 4: Huffman Coding
"""
Greedy choice:
Repeatedly merge the two least frequent symbols.

Guarantees minimum weighted path length.
"""

# 6. Greedy vs Dynamic Programming

"""
-----------------------------------------------------------------------------
Aspect	          |         Greedy	            |        Dynamic Programming
-----------------------------------------------------------------------------
Decisions	      |         Local	            |        Global
Backtracking	  |         No	                |        Yes
Speed	          |         Very fast	        |        Slower
Memory	          |         Low	                |        Higher
Correctness	      |         Problem-specific	|        Guaranteed

Rule of thumb:

If greedy can be proven, use it

Otherwise, use DP
"""

# 7. How to prove a Greedy algorithm is correct

"""
Technique 1: Exchange Argument
Show that any optimal solution can be transformed into the greedy solution 
without making it worse.

Technique 2: Cut & Paste Proof
Show that the greedy choice must appear in some optimal solution.

Technique 3: Matroid Theory (advanced)
Used in scheduling and spanning trees.
"""

# 8. Famous Greedy algorithms

"""
Kruskal’s Minimum Spanning Tree
Prim’s Minimum Spanning Tree
Dijkstra’s Shortest Path (with non-negative edges)
Huffman Coding
Interval Scheduling
Job Sequencing with Deadlines
Gas Station problem
Jump Game
"""

# 9. How to recognize a Greedy problem

"""
Ask yourself:

Can I sort the input meaningfully?
Does a local choice reduce the problem optimally?
Does the decision affect future options monotonically?

If yes → Greedy is likely viable.
"""

# 10. Definition one-liner

"""
A Greedy Algorithm constructs a solution by repeatedly making locally optimal choices, 
relying on problem structure to guarantee global optimality.
"""

# 11. Key insight to remember

"""
Greedy is fast, elegant, and dangerous if unproven.
"""
