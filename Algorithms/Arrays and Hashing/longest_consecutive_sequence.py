# Leetcode 128. Longest Consecutive Sequence

# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        total = 0

        for num in nums_set:
            value = num
            if value - 1 not in nums_set:
                while value in nums_set:
                    value += 1
                total = max(total, value - num)
        return total

# O(n) Time complexity
# O(n) Space complexity

soluton = Solution()

print(soluton.longest_consecutive([100,4,200,1,3,2])) # 4
print(soluton.longest_consecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(soluton.longest_consecutive([1,0,1,2])) # 3
print(soluton.longest_consecutive([])) # 0