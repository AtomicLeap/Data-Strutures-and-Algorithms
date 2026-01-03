# Leetcode 3788. Maximum Score of a Split

# https://leetcode.com/problems/maximum-score-of-a-split/description/

def max_score(nums: list[int]) -> int:
    n = len(nums)
    prefix_arr = [0]
    score = []
    min_val = max(nums)
    suffix = [min_val] * n

    for i in range(n):
        prefix_arr.append(prefix_arr[-1] + nums[i])
    for i in range(n - 1, -1, -1):
        suffix[i] = min_val
        min_val = min(nums[i], min_val)
    for i in range(n - 1):         
        score.append(prefix_arr[i + 1] - suffix[i])
    return max(score)

# Time complexity  - O (n)
# Space complexity  - O (n)

print(max_score([10,-1,3,-4,-5])) # 17
print(max_score([-7,-5, 3])) # -2
print(max_score([1, 1])) # 0
