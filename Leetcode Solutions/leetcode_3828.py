# Leetcode 3828. Final Element After Subarray Deletions

# https://leetcode.com/problems/final-element-after-subarray-deletions/description/

def final_remaining_element(nums: list[int]) -> int:
    return max(nums[0], nums[-1])

# O(1) - Time complexity
# O(1) - Space complexity

print(final_remaining_element([1, 5, 2])) # 2
print(final_remaining_element([3, 7])) # 7