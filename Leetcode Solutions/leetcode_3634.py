# Leetcode 3634. Minimum Removals to Balance Array

# https://leetcode.com/problems/minimum-removals-to-balance-array/description

# Two Pointer Solution
def min_removal(nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        best = 1

        for right in range(n):
            # shrink window until balanced
            while nums[right] > nums[left] * k:
                left += 1
            best = max(best, right - left + 1)

        return n - best
# Complexity
# Sorting: O(n log n)
# Two-pointer scan: O(n)
# O(n log n) - Time complexity

# O(1) - Space complexity

print(min_removal([2,1,5], k = 2)) # 1
print(min_removal([1,6,2,9], k = 3)) # 2
print(min_removal([4,6], k = 2)) # 0