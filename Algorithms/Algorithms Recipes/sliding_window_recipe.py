# Sliding Window Recipe

# 1. What is the Sliding Window technique?

"""
Sliding Window is an optimization technique used to process contiguous 
subarrays or substrings efficiently. Instead of recomputing information for 
every possible subarray from scratch, you:

1. Maintain a window (a range [left, right])
2. Expand the window to include new elements
3. Shrink the window to remove old elements
4. Update your answer incrementally

This reduces time complexity from O(n²) to O(n) in many problems.
"""
# 2. When should you think of Sliding Window?

"""
Use Sliding Window when:

1. You are dealing with arrays or strings
2. The problem involves contiguous elements
3. You need max / min / count / sum / frequency over a range
4. The constraints allow two pointers moving forward

Typical phrases in problems:

“subarray”,“substring”, “contiguous”, “at most k”, “longest / shortest”, “window”.
"""
# 3. Two main types of Sliding Window

"""
Type 1: Fixed-size window
The window size k is constant.

Example:
Maximum sum of any subarray of size k

-> Naive
For each i:
    sum elements from i to i+k-1   → O(nk)

-> Sliding Window
Compute first window sum
Slide window:
    add next element
    remove previous element

-> Pseudocode
window_sum = sum(arr[0:k])
max_sum = window_sum

for r in range(k, n):
    window_sum += arr[r]
    window_sum -= arr[r - k]
    max_sum = max(max_sum, window_sum)

-> Time: O(n)
-> Space: O(1)

Type 2: Variable-size window (most important)
The window grows and shrinks dynamically based on a condition.

This uses two pointers:
left → start of window
right → end of window

General pattern
left = 0
for right in range(n):
    add arr[right] to window

    while window is invalid:
        remove arr[left]
        left += 1

    update answer using window [left, right]
"""

# 4. Core idea (mental model)

"""
Think of it like a camera frame sliding over a scene:
right moves forward → expanding
left moves forward → contracting

Window never moves backward
Each element enters and leaves the window once

That’s why it’s O(n).
"""

# 5. Classic Sliding Window examples

"""
Example 1: Longest substring without repeating characters

Problem:
Find the longest substring with all unique characters.

Idea:

Expand right
If duplicate found → move left until valid

seen = set()
left = 0
ans = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    seen.add(s[right])
    ans = max(ans, right - left + 1)


Example 2: Longest substring with at most k replacements

Key invariant:
window_size - max_frequency <= k

-> Expand window
-> Shrink when invalid
-> Track best length
"""

# 6. How to recognize it in interviews

"""
Ask yourself:

1. Is the data contiguous? 
2. Can I maintain a condition incrementally?
3. Can both pointers move only forward?

If yes → Sliding Window
Sliding Window works only for contiguous data
"""

# 7. One-sentence definition
"""
Sliding Window is a technique that uses two pointers to maintain a dynamic range 
over contiguous elements, allowing efficient incremental computation of subarray 
or substring properties in linear time.
"""