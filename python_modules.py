# Python built-in modules and Standard Libraries

"""
Some Python built-in modules and standard-library tools that can massively simplify and speed up work — both conceptually and in coding time.
"""

# 1. collections — Specialized Data Structures

"""
The go-to module for many algorithmic tasks.

----------------------------------------------------------------------------------------------------------
Class	        What It Does	                                    Common Use Cases
----------------------------------------------------------------------------------------------------------
deque	        Double-ended queue (O(1) append/pop both ends)	    BFS, sliding windows, queues
Counter	        Frequency counting	                                Hash-map frequency, majority elements
defaultdict	    Dict with automatic default value	                Graph adjacency list, grouping
namedtuple	    Lightweight object for tuples with names	        Immutable records (e.g. edges)
OrderedDict	    Dict that remembers insertion order (pre-3.7)	    LRU cache, order-sensitive maps
"""
# Example - BFS with deque
"""
from collections import deque

q = deque([start])
while q:
    node = q.popleft()
    for nei in graph[node]:
        q.append(nei)

"""
# Example - Frequency counting

from collections import Counter

freq = Counter([1,2,2,3,3,3])
print(freq)  # Counter({3:3, 2:2, 1:1})


# 2. heapq — Priority Queues / Heaps
"""
Implements a min-heap using a simple list.
--------------------------------------------------------------------------------------
Function	                    Description
--------------------------------------------------------------------------------------
heappush(heap, val)	            Push new element
heappop(heap)	                Pop smallest element
heapify(list)	                Convert list to heap in O(n)
nlargest(n, iterable)	        Return n largest elements
nsmallest(n, iterable)	        Return n smallest elements

"""
# Example - Dijkstra’s Algorithm
"""
import heapq

pq = [(0, start)]  # (distance, node)
while pq:
    dist, node = heapq.heappop(pq)
    for nei, w in graph[node]:
        heapq.heappush(pq, (dist + w, nei))
"""


# 3. bisect — Binary Search Utilities
"""
Used for maintaining sorted arrays, Longest Increasing Subsequence problems, and efficient lookups.

-----------------------------------------------------------------------
Function	            Description
-----------------------------------------------------------------------
bisect_left(a, x)	    First index where x can go (≥x)
bisect_right(a, x)	    Index after last occurrence of x
insort_left(a, x)	    Insert at leftmost position keeping sorted order
insort_right(a, x)	    inserts at rightmost position keeping sorted order
"""
# Example - find index of lower/upper bounds

from bisect import bisect_left, bisect_right

arr = [1,3,4,6,8]
print(bisect_left(arr, 4))  # 2
print(bisect_right(arr, 4)) # 3


# 4. itertools — Combinatorial Utilities

"""
Perfect for permutations, combinations, and iterator tricks.

---------------------------------------------------------------------------
Function	                    Purpose
---------------------------------------------------------------------------
permutations(iterable, r)	    All orderings of r elements
combinations(iterable, r)	    All r-length subsets
product(*iterables)	            Cartesian product
accumulate(iterable)	        Running sums (prefix sums)
groupby(iterable)	            Group consecutive elements
"""
# Example - generate all subsets

from itertools import combinations

nums = [1,2,3]
for r in range(len(nums) + 1):
    for subset in combinations(nums, r):
        print(subset)


# Example - prefix sums

from itertools import accumulate

nums = [1,2,3,4]
print(list(accumulate(nums)))  # [1,3,6,10]


# 5. functools — Functional Tools

"""
--------------------------------------------------------------
Tool	            Purpose
--------------------------------------------------------------
lru_cache	        Memoization (great for DP recursion)
reduce	            Fold a function across an iterable
cmp_to_key	        Convert compare function to sort key
"""

# Example - Memoization in DP

from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n < 2: return n

    return fib(n - 1) + fib(n - 2)


# 6. math — Mathematical Utilities

"""
Essential for numeric and geometric problems.

----------------------------------------------------------------
Function	                            Purpose
----------------------------------------------------------------
sqrt, pow, gcd, lcm, ceil, floor	    Basic math ops
inf, isinf, isnan	                    Infinity handling
factorial, comb	                        Combinatorial math
"""
# Example

import math

print(math.gcd(20, 8))     # 4
print(math.comb(5, 2))     # 10
print(math.inf > 1e18)     # True


# 7. statistics — Basic Statistical Analysis

"""
Useful for average, median, mode — occasionally used in algorithmic reasoning.
"""
import statistics as st

data = [1, 2, 2, 3, 4]
print(st.mean(data))   # 2.4
print(st.median(data)) # 2
print(st.mode(data))   # 2


# 8. random — Randomized Algorithms

"""
Monte-Carlo simulations, randomized quicksort, shuffling, sampling.
"""
import random

arr = [1,2,3,4,5]
random.shuffle(arr)
print(random.choice(arr))
print(random.sample(arr, 3))


# 9. array and queue

"""
array — efficient numeric arrays (memory-friendly vs. list)

queue.Queue — thread-safe FIFO (used rarely in competitions but common in BFS)
"""
from array import array

nums = array('i', [1,2,3])
print(nums[1])  # 2


# 10. graphlib (Python 3.9+)

"""
Provides TopologicalSorter for DAGs — great for dependency problems.
"""
from graphlib import TopologicalSorter

g = {3: [1, 2], 2: [1], 1: []}
order = list(TopologicalSorter(g).static_order())
print(order)  # [1, 2, 3]


# Summary -> 
# -> Learn to recognize patterns: 
#       BFS → deque, DP recursion → lru_cache, greedy → heapq, binary search → bisect.
# -> Use built-in modules to avoid reinventing data structures — they’re all O(log n) or O(1) optimized in C.