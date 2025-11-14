# Heap

"""
What is a Heap?
A Heap is a special tree-based data structure that satisfies the heap property:

The parent node's value is always ordered with respect to its children.
It is commonly implemented using an array, not actual tree nodes, because the 
shape is always a complete binary tree.
"""

# Properties of a Heap
"""
1. Complete Binary Tree
 - All levels are fully filled except possibly the last.
 - The last level is filled from left to right.

2. Heap Property
 - Determines whether it is a min-heap or max-heap.

3. Efficient operations
 - Insert: O(log n)
 - Remove root: O(log n)
 - Peek root: O(1)

"""

# Min-Heap

"""
A min-heap ensures:
1. The smallest element is always at the root.

2. For every node: - parent ≤ child
"""

# Example min-heap:

"""
        1
      /   \
     3     5
    / \   / \
   4  8  6  10

Root (1) is the smallest.

Every parent is ≤ its children.
"""

# Uses

"""
1. Priority Queues (extract min)
2. Dijkstra’s algorithm
3. A* search
4. CPU scheduling
5. Memory management
"""

# Max-Heap

"""
The opposite of min-heap:
1. The largest element is always at the root.
2. For every node: - parent ≥ child

"""

# Example:
"""
       10
      /  \
     7    5
    / \  / \
   4  1 3  2
"""

# Uses

"""
Selection problems (find k largest)
Heap-sort
Scheduling
"""

# Why Use Heaps?

"""
1. Fast insertion & removal of the highest/lowest priority item.
2. Faster than sorting every time.
3. More efficient than an unsorted list or sorted array for dynamic workloads.

----------------------------------------------------------------------------
Operation	    |   Min/Max Heap |   Sorted List	|   Unsorted List
----------------------------------------------------------------------------
Insert	       |   O(log n)	   |   O(n)	         |   O(1)   
Get Min/Max	    |   O(1)	      |   O(1)	         |   O(n)    
Remove Min/Max	 |   O(log n)     |	 O(n)	         |   O(n)    

"""

# How a heap is stored (array layout)
"""
A heap does not need pointers.

Given parent index i:
-------------------------------------------
Relationship	     Index
-------------------------------------------
Left child	        2*i + 1
Right child	        2*i + 2
Parent	           (i - 1) // 2

Example heap array:

[1, 3, 5, 4, 8, 6, 10]

Represents:

         1
      /     \
     3       5
    / \     / \
   4  8    6   10
"""

# Heap Methods

"""
1. heapq.heappushpop(heap, item)
 - Push item, then pop and return the smallest from the heap.
 - Push → Pop (optimized)
 - But if item is smaller than current min, that item will be returned immediately and not added to the heap.

2. heapq.heapreplace(heap, item)
 - Pop and return smallest, then push item into heap.
 - Pop → Push
 - Always pushes item
 - Does not compare item with smallest — unlike heappushpop

"""

# Summary

"""
------------------------------------------------------------------------------------------
Feature	        |        Min-Heap	              |      Max-Heap
------------------------------------------------------------------------------------------
Root	           |     Smallest element	        |    Largest element
Property	        |    parent ≤ children	        |    parent ≥ children
Used for	        |    extract-min, Dijkstra, PQ	  |  extract-max, heap sort, k-largest

A heap is a tree structure stored in an array that always maintains either 
smallest or largest element at the top, with efficient insertion & removal.
"""