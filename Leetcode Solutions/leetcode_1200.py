# Leetcode 1200. Minimum Absolute Difference

# https://leetcode.com/problems/minimum-absolute-difference/description/

def min_abs_difference(arr: list[int])->list[int]:
    n = len(arr)
    min_diff = float('inf')
    arr.sort()
    results = []
    for idx in range(1, n):
        diff = arr[idx] - arr[idx - 1]
        min_diff = min(min_diff, diff)
    
    for idx in range(1, n):
        diff = arr[idx] - arr[idx - 1]
        if diff == min_diff:
            results.append([arr[idx - 1], arr[idx]])
    return results

# O(n log n) - Time complexity
# O(1) - Space complexity

print(min_abs_difference([4,2,1,3])) # [[1,2],[2,3],[3,4]]
print(min_abs_difference([1,3,6,10,15])) # [[1,3]]
print(min_abs_difference([3,8,-10,23,19,-4,-14,27])) # [[-14,-10],[19,23],[23,27]]
