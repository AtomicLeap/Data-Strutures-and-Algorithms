# Bisect Recipe

# What is bisect in Python?
"""
bisect is a built-in Python module that helps you:

1. Maintain a sorted list efficiently.
2. Find insertion points for new elements (using binary search).
3. Insert elements into a sorted list at the correct position.

It avoids you having to sort every time you insert something — instead, 
you can binary search the correct position in O(log n) time.
"""

# Importing
"""
import bisect

Now you can use:

1. bisect_left()
2. bisect_right()
3. insort_left()
4. insort_right()
"""

# bisect_left(list, num)

"""
Finds the insertion index to insert x into list while keeping it sorted —
it returns the first index where x can go without breaking order.

If x already exists in the list, it returns the leftmost index.
"""
from bisect import bisect_left

arr = [1, 3, 4, 4, 5]
i = bisect_left(arr, 4)
print(i)  # Output: 2

"""
Explanation:

Indexes:   0  1  2  3  4
Values:   [1, 3, 4, 4, 5]
                 ^
                 └── first position where 4 could go


So inserting at index 2 keeps the list sorted.
"""

# bisect_right(list, num) (aka bisect())

"""
Similar, but it returns the index after the rightmost occurrence of x.
"""
from bisect import bisect_right

arr = [1, 3, 4, 4, 5]
i = bisect_right(arr, 4)
print(i)  # Output: 4

"""
Explanation:

Indexes:   0  1  2  3  4
Values:   [1, 3, 4, 4, 5]
                       ^
                       └── after last 4

So inserting at index 4 would place the new 4 after existing ones.
"""

# Summary of Difference
"""
--------------------------------------------------------------------------------------------------------------------------
Function	        |   If element already exists	|   Insertion position	|   Example result for arr = [1,3,4,4,5], x=4
--------------------------------------------------------------------------------------------------------------------------
bisect_left	        |   before existing elements	|   leftmost possible	|   index = 2
bisect_right/bisect |   after existing elements	    |   rightmost possible	|   index = 4
"""

# insort_left() and insort_right()
"""
They insert directly into the list at the proper position (keeping it sorted).
"""

from bisect import insort_left, insort_right

arr = [1, 3, 4, 4, 5]

insort_left(arr, 4)
print(arr)   # [1, 3, 4, 4, 4, 5]

arr = [1, 3, 4, 4, 5]
insort_right(arr, 4)
print(arr)   # [1, 3, 4, 4, 4, 5] (same but placed after existing 4s)

# NOTE
"""
bisect_left and bisect_right -> returns the index where element can be inserted 
                                without distorting the sorted nature of the list

insort_left and insort_right -> return void. They insert the element at the
                                appropriate index, but returns None(Null).                             
                                
"""
# Common Uses of bisect
"""
-------------------------------------------------------------------------------------------
        Use Case	                        |          Description
-------------------------------------------------------------------------------------------
1. Maintaining sorted lists	                |   Efficiently insert while keeping order.
2. Binary search utilities	                |   Quickly find lower/upper bounds.
3. Longest Increasing Subsequence (LIS)	    |   To replace the first element ≥ x (via bisect_left).
4. Range counting	                        |   To find how many numbers fall in [low, high) using two bisect calls.
5. Leaderboard or ranking systems	        |   To insert new scores in sorted order efficiently.
"""

# Example – Range Counting

"""
Suppose we have a sorted list of scores:
"""

scores = [20, 35, 40, 50, 60, 75, 90]

"""
Find how many scores are between 40 and 70:
"""

from bisect import bisect_left, bisect_right

low = bisect_left(scores, 40)   # first index ≥ 40 → 2
high = bisect_right(scores, 70) # first index > 70 → 5

count = high - low
print(count)  # Output: 3  (40, 50, 60)

# Example – Longest Increasing Subsequence LIS

"""
We use bisect_left because:
1. We want to replace the first element ≥ x (to keep subsequence strictly 
    increasing).
2. It gives the smallest possible tail for subsequences of that length.
"""

from bisect import bisect_left

nums = [10,9,2,5,3,7,101,18]
tails = []

for num in nums:
    i = bisect_left(tails, num)
    if i == len(tails):
        tails.append(num)
    else:
        tails[i] = num
print(tails)  # [2, 3, 7, 18]

# Summary Table
"""
---------------------------------------------------------------------------------------------------
    Function	        |         Returns	                |   Purpose
---------------------------------------------------------------------------------------------------
bisect_left(arr, num)	|   leftmost insertion index	    |   first index where arr[i] >= num
bisect_right(arr, num)	|   rightmost insertion index	    |   first index where arr[i] > num
insort_left(arr, num)	|   inserts at leftmost position	|   keeps list sorted
insort_right(arr, num)	|   inserts at rightmost position	|   keeps list sorted
"""

# In short:
"""
-> Use bisect_left when you need strictly increasing sequences or lower bounds.
-> Use bisect_right when you want non-decreasing or upper bounds.
"""
