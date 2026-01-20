# Leetcode 15. 3Sum

# https://leetcode.com/problems/3sum/description/

# Two pointer solution
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        # Pruning: since array is sorted, if nums[i] > 0, sum can't be 0
        if nums[i] > 0:
            break
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            sum_total = nums[i] + nums[left] + nums[right]
            if sum_total == 0: # Happy path
                result.append([nums[i], nums[left], nums[right]])
                # Move both pointers
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif sum_total < 0:
                left += 1
            else:
                right -= 1

    return result


# n = len(nums)
# O(n^2) - Time complexity -> Sorting O(n log n) + two-pointer scan O(n²) ⇒ overall O(n²) time;
#  O(1) - Space complexity ->  O(1) extra space (excluding output - result).

print(three_sum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(three_sum([0,1,1])) # []
print(three_sum([0,0,0])) # [[0,0,0]]


# Iterative solution

def three_sum_i(nums: list[int])-> list[list[int]]:
    n = len(nums)
    results = set()
    nums.sort()


    for idx, num in enumerate(nums):
        if num > 0:
            break
        left, right = idx + 1, n - 1
        while left < right:
            sum_total = num + nums[left] + nums[right]
            if sum_total == 0:
                results.add((num, nums[left], nums[right]))
                left += 1
                right -= 1
            elif sum_total < 0:
                left += 1
            else:
                right -= 1
    return [list(result) for result in results]

# n = len(nums)
# O(n^2) - Time complexity -> Sorting O(n log n) + two-pointer scan O(n²) ⇒ overall O(n²) time;
#  O(1) - Space complexity ->  O(1) extra space (excluding output - result)

print(three_sum_i([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(three_sum_i([0,1,1])) # []
print(three_sum_i([0,0,0])) # [0,0,0]