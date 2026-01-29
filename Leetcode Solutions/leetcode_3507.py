# Leetcode 3507. Minimum Pair Removal to Sort Array I

# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description

def minimum_pair_removal(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    a = list(map(int, nums))  # work on a copy
    ops = 0

    def is_non_decreasing(arr: list[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                return False
        return True

    while not is_non_decreasing(a):
        m = len(a)
        best_sum = float('inf')
        best_idx = -1

        # Find adjacent pair with minimum sum (leftmost on ties)
        for i in range(m - 1):
            s = a[i] + a[i + 1]
            if s < best_sum:
                best_sum = s
                best_idx = i

        # Build new array with the chosen pair merged
        b = []
        i = 0
        while i < m:
            if i == best_idx:
                b.append(best_sum)
                i += 2  # skip the next element (merged)
            else:
                b.append(a[i])
                i += 1

        a = b
        ops += 1

    return ops

# O(n²) - Time complexity
# O(n) - Space complexity

print(minimum_pair_removal([5, 2, 3, 1]))  # 2
print(minimum_pair_removal([1, 2, 2]))     # 0
