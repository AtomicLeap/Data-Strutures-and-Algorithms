# Two Pointers Recipe

# 1. What is the Two Pointers technique?

"""
Two Pointers is a strategy where you use two indices (pointers) to traverse a data structure,
most commonly an array or string, in a coordinated way to avoid nested loops.

Instead of checking all pairs or ranges explicitly (O(n²)), you move pointers 
intelligently to achieve O(n) or O(n log n) solutions.
"""

# 2. When should you think of Two Pointers?

"""
Use Two Pointers when:

1. You’re working with arrays or strings.
2. You need to compare, pair, or shrink ranges.
3. The structure is sorted or can be processed sequentially.
4. You want to eliminate brute-force nested loops.

Typical keywords in problems:

“pair”, “two numbers”, “sorted”, “remove duplicates”, “palindrome”, “merge”,
“container”, “closest / target sum”.
"""

# 3. Core idea (mental model)

"""
Think of two people starting at different positions and walking toward a goal, 
adjusting their direction based on what they see.

Pointers can move:
1. toward each other
2. in the same direction
3. at different speeds

Each pointer moves at most n times, so total work is linear.
"""

# 4. Main patterns of Two Pointers

# Pattern 1: Opposite-direction pointers (most common)
"""
Pointers start at both ends.

Used when:

1. Array is sorted
2. You are searching for a pair
3. You want to shrink a range optimally

Example: Two Sum (sorted array)

l, r = 0, n - 1

while l < r:
    s = arr[l] + arr[r]

    if s == target:
        return True
    elif s < target:
        l += 1
    else:
        r -= 1

Why it works:

If sum is too small → increase left pointer
If sum is too large → decrease right pointer
"""

# Pattern 2: Same-direction pointers (slow & fast)

"""
Both pointers move forward, but at different speeds.

Used when:

1. Removing elements
2. Compressing arrays
3. Filtering data in place

Example: Remove duplicates (sorted array)

slow = 0

for fast in range(1, n):
    if arr[fast] != arr[slow]:
        slow += 1
        arr[slow] = arr[fast]

After loop:

Elements [0..slow] are unique
"""

# Pattern 3: Sliding window (specialized two pointers)

"""
Here, Two Pointers become a window.

left shrinks
right expands

Window maintains a condition

left = 0
for right in range(n):
    add(arr[right])

    while invalid:
        remove(arr[left])
        left += 1

--> Sliding Window is a subset of Two Pointers.
"""

# Pattern 4: Fast & slow cycle detection

"""
Pointers move at different speeds.

Used for:

1. Detecting cycles
2. Finding middle of linked list

Example: Floyd’s cycle detection
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
"""

# 5. Why Two Pointers works (intuition)

"""
Instead of re-checking combinations:

Each pointer move eliminates a set of impossible solutions
Decisions are made based on monotonic properties (sortedness, uniqueness, bounds)
This guarantees efficiency.
"""

# 6. Sliding Window vs Two Pointers

"""
--------------------------------------------------------------------------
Feature	        |       Two Pointers	     |      Sliding Window
--------------------------------------------------------------------------
Pointers	    |       Any movement	     |      Usually forward
Window size	    |       Fixed or dynamic	 |      Dynamic
Constraints	    |       Pair / range logic	 |      Window validity
Relationship	|       General technique	 |      Specialized form
"""

# 7. Definition (one-liner)

"""
Two Pointers is a technique that uses two indices moving through a data structure 
in a coordinated way to reduce nested loops and solve problems efficiently in linear time.
"""

# 8. How to identify Two Pointers problems quickly

"""
Ask yourself:

1. Can pointers move based on a condition?
2. Is the structure ordered or monotonic?
3. Can one pointer eliminate multiple candidates at once?

If yes → Two Pointers
"""

# 9. Key insight to remember

"""
Sliding Window ⊂ Two Pointers
Fast–slow ⊂ Two Pointers
Opposite ends ⊂ Two Pointers

Two Pointers is the umbrella technique.
"""
