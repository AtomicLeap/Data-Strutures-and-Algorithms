# Leetcode 53. Maximum Subarray

"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using 
the divide and conquer approach, which is more subtle
"""

# Kadane's Algorithm
"""
Idea: scan once while keeping curr = best sum ending at current index,
best = best sum seen so far.
At each step, either extend the current subarray or start fresh at nums[i].
"""
def max_subarray(nums):
    curr = best = nums[0]
    for x in nums[1:]:
        curr = max(x, curr + x)  # extend or restart
        best = max(best, curr)
    return best

# n = len(nums)
# O(n) - Time complexity
# O(1) - Space complexity


# Divide and Conquer Algorithm
def max_subarray_divide_and_conquer(nums):
    def solve(lo, hi):
        if lo == hi:
            x = nums[lo]
            return (x, x, x, x)  # tot, pref, suff, best

        mid = (lo + hi) // 2
        Lt, Lp, Ls, Lb = solve(lo, mid)
        Rt, Rp, Rs, Rb = solve(mid + 1, hi)

        tot = Lt + Rt
        pref = max(Lp, Lt + Rp)
        suff = max(Rs, Rt + Ls)
        best = max(Lb, Rb, Ls + Rp)
        return (tot, pref, suff, best)

    return solve(0, len(nums) - 1)[3]

# n = len(nums)
# O(n) - Time complexity
# O(log n) - Space complexity --> Recusive stack

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(max_subarray([1])) # 1
print(max_subarray([5,4,-1,7,8])) # 23

print(max_subarray_divide_and_conquer([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(max_subarray_divide_and_conquer([1])) # 1
print(max_subarray_divide_and_conquer([5,4,-1,7,8])) # 23