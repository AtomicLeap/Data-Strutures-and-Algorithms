# Leetcode 3719. Longest Balanced Subarray I

# https://leetcode.com/problems/longest-balanced-subarray-i/description

# Brute - Force Approach -> Two Pointer
def longest_balanced(nums: list[int]) -> int:
    n = len(nums)
    result = 0

    for left in range(n):
        even_set = set()
        odd_set = set()
        count = 0
        for right in range(left, n):
            num = nums[right]
            if num & 1:
                odd_set.add(num)
            else:
                even_set.add(num)
            if len(odd_set) == len(even_set):
                count = right - left + 1
                result = max(result, count)
    return result

# O(n^2) - Time complexity
# O(n) - Space complexity


# Optimized Solution

def longest_balanced_i(nums: list[int]) -> int:
    n = len(nums)
    max_value = max(nums)

    last_even = [0] * (max_value + 1)
    last_odd  = [0] * (max_value + 1)

    results = 0

    for left in range(n):
        marker = left + 1   # unique stamp for this left boundary
        distinct_even = distinct_odd = 0      # distinct even / distinct odd counts in nums[left..right]

        for right in range(left, n):
            num = nums[right]
            if num & 1:  # odd
                if last_odd[num] != marker:
                    last_odd[num] = marker
                    distinct_odd += 1
            else:      # even
                if last_even[num] != marker:
                    last_even[num] = marker
                    distinct_even += 1

            if distinct_even == distinct_odd:
                results = max(results, right - left + 1)

    return results

# O(n^2) - Time complexity
# O(max(nums)) - Space complexity - for the stamp arrays (≤ 100001)

print(longest_balanced([2,5,4,3])) # 4
print(longest_balanced([3,2,2,5,4])) # 5
print(longest_balanced([1,2,3,2])) # 3

print(longest_balanced_i([2,5,4,3])) # 4
print(longest_balanced_i([3,2,2,5,4])) # 5
print(longest_balanced_i([1,2,3,2])) # 3
