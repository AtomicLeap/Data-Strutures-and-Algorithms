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

This allows Binary Search on the answer, even when data isn't explicitly sorted.
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

def binary_search(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

Complexity => 
Time: O(log n)
Space: O(1)
"""

# 5. Binary Search for boundaries (most important)

"""
Most interview problems are not exact match searches.
Instead, they ask for:

1. First occurrence
2. Last occurrence
3. Smallest valid index
4. Largest feasible value

Example: First index ≥ target
def lower_bound(arr: list[int], target: int) -> int:
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
"""

# 6. Binary Search on the Answer

"""
Used when the answer space is numeric and feasibility is monotonic.

Pattern
def feasible(x):
    return True or False  # monotonic

left, right = min_possible, max_possible
while left < right:
    mid = (left + right) // 2
    if feasible(mid):
        right = mid
    else:
        left = mid + 1
return left

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
Binary Search is not about arrays — it's about monotonicity.
"""

# 12. Final mental checklist

"""
Before using Binary Search, ask:

1. Is the data sorted?
2. Or is the answer space monotonic?
3. Can I write a feasible(mid) function?

If yes → Binary Search
"""

# 13. When Should Binary Search Click in Your Mind?
"""
Think Binary Search when you see:

-> Sorted array / rotated sorted array
-> Minimum / Maximum answer
-> Capacity / speed / days / size
-> "Can we do it?" → Yes / No type logic
-> If the answer looks like:
    false false false true true true

Then, Binary Search is the correct approach.
"""

# Most Generalized Binary Search Template

# https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8/

"""
Suppose we have a search space. It could be an array, a range, etc. Usually it's 
sorted in ascending order. For most tasks, we can transform the requirement into 
the following generalized form:

Minimize k , such that condition(k) is True

The following code is the most generalized binary search template:

def binary_search(array: list[int]) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left

What's really nice of this template is that, for most of the binary search problems, 
we only need to modify three parts after copy-pasting this template, and never need 
to worry about corner cases and bugs in code any more:

1. Correctly initialize the boundary variables left and right to specify 
    search space. Only one rule: set up the boundary to include "all possible elements"
2. Decide return value. Is it "return left" or "return left - 1"? 
    Remember this: after exiting the while loop, left is the "minimal k satisfying the condition function";
3. Design the condition function. This is the most difficult and most beautiful part. Needs lots of practice.
"""
