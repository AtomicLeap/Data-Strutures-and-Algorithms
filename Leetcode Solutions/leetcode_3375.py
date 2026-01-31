# Leetcode 3375. Minimum Operations to Make Array Values Equal to K

# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/


# Key Idea
"""
This operation can only decrease numbers (never increase). 
Also, you can only decrease the current maximum value(s) down to some h that 
is at least the current second-maximum, because h is valid iff all numbers 
strictly greater than h are identical (i.e., there is only one “level” above h).

So the process is essentially:
1. Repeatedly remove the largest distinct value by lowering it to the next 
    lower distinct value,
2. until everything becomes equal to some constant,
3. and possibly one last step to lower that constant to k.

When is it impossible?
If any element is < k, it's impossible because you can't increase it.

So:
1. If min(nums) < k → answer is -1.

# Minimum number of operations
Let the sorted distinct values be:
v1 < v2 < ... < vm, where v1 = min(nums) and m = #distinct values.

There are two possible cases (given min(nums) >= k):
1. Case 1: k == v1 (k equals the minimum)
You cannot change the minimum, so you must bring all higher distinct 
    values down to k.
Each operation removes one distinct level above k.
-> Answer = number of distinct values > k = m - 1.

2. Case 2: k < v1 (k is smaller than the minimum)
First, you must make the array constant at v1 (can't touch v1 until everything 
else becomes v1).
That takes m - 1 operations.

Then, since all values are identical (v1), you can lower them all to k in one 
final operation.
-> Answer = (m - 1) + 1 = m.

# Algorithm (O(n))
1. If any x < k, return -1.
2. Let S = set(nums), m = len(S), mn = min(nums).
3. If k == mn: return count of values in S greater than k.
4. Else (k < mn): return m.
"""
def min_operations(nums: list[int], k: int) -> int:
    # cannot increase numbers
    if any(num < k for num in nums):
        return -1

    distinct_nums = set(nums)
    m = len(distinct_nums)
    min_val = min(nums)

    if k == min_val:
        return sum(1 for num in distinct_nums if num > k) # Alternatively return m - 1
    else:  # k < min_val
        return m

# O(n) - Time complexity
# O(n) - Space complexity

print(min_operations([5,2,5,4,5], 2)) # 2
print(min_operations([2,1,2], 2)) # -1
print(min_operations([9,7,5,3], 1)) # 4
