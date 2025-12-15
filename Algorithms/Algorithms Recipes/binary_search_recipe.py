# Binary Search Recipe

# 1. What is Binary Search?

"""
Binary Search is a divide-and-conquer algorithm used to search efficiently in 
a sorted or monotonic space by repeatedly halving the search range.

Core idea:
Eliminate half of the remaining search space at each step.
"""

# 2. When can Binary Search be used?

"""
Binary Search works only if one of these is true:

1. Sorted Data
The array or list is sorted (ascending or descending).

2. Monotonic Predicate
There exists a function f(x) such that:

False, False, False, True, True, True

Once True starts, it stays True.

This allows Binary Search on the answer, even when data isn’t explicitly sorted.
"""

# 3. Intuition (mental model)

"""
Think of guessing a number between 1 and 100:

Guess 50 → “too high”
Guess 25 → “too low”
Guess 37 → “correct”

Each guess cuts the search space in half.
"""

# 4. Classic Binary Search (exact match)

"""
Goal -> Find target in a sorted array.

Algorithm

-> Compare middle element with target
-> Discard half of the array
-> Repeat

Code - Implementation

def binary_search(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1

Complexity => 
Time: O(log n)
Space: O(1)
"""

# 5. Binary Search for boundaries (most important)

"""
Most interview problems are not exact match searches.
Instead, they ask for:

First occurrence
Last occurrence
Smallest valid index
Largest feasible value

Example: First index ≥ target
def lower_bound(arr, target):
    l, r = 0, len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l
"""

# 6. Binary Search on the Answer

"""
Used when the answer space is numeric and feasibility is monotonic.

Pattern
def feasible(x):
    return True or False  # monotonic

l, r = min_possible, max_possible
while l < r:
    mid = (l + r) // 2
    if feasible(mid):
        r = mid
    else:
        l = mid + 1
return l

Examples

-> Capacity to ship packages in D days
-> Koko eating bananas
-> Minimize maximum distance
-> Split array largest sum
"""

# 7. Why Binary Search works (invariant)

"""
At every step:

Answer ∈ [left, right]

Each comparison preserves the invariant while halving the interval.
"""

# 8. Common Binary Search variants

"""
--------------------------------------------------------------------
Variant	                 |               Purpose
--------------------------------------------------------------------
Exact match	             |               Find element
Lower bound	             |               First ≥ target
Upper bound	             |               First > target
First true	             |               Monotonic boolean
Last true	             |               Reverse monotonic
Peak finding	         |               Unimodal arrays
"""

# 9. Binary Search vs other techniques

"""
------------------------------------------------------------------------
Technique	              |              When to use
------------------------------------------------------------------------
Binary Search	          |              Monotonic space, sorted data
Two Pointers	          |              Pair / linear elimination
Sliding Window	          |              Dynamic contiguous ranges
Dynamic Programming (DP)  |              Overlapping subproblems
"""

# 10. Definition (one-liner)

"""
Binary Search is a logarithmic-time algorithm that finds a target or boundary 
in a sorted or monotonic search space by repeatedly halving the range.
"""

# 11. Key insight to remember

"""
Binary Search is not about arrays — it’s about monotonicity.
"""

# 12. Final mental checklist

"""
Before using Binary Search, ask:

1. Is the data sorted?
2. Or is the answer space monotonic?
3. Can I write a feasible(mid) function?

If yes → Binary Search
"""
