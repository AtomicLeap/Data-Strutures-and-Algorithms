# Leetcode 4. Median of Two Sorted Arrays

# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Tags -> Array, Binary Search, Divide and Conquer

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    A, B = nums1, nums2
    m, n = len(A), len(B)

    # Always binary search the smaller array
    if m > n:
        A, B = B, A
        m, n = n, m

    total = m + n
    half = (total + 1) // 2

    lo, hi = 0, m
    NEG_INF = float("-inf")
    POS_INF = float("inf")

    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i

        a_left  = A[i - 1] if i > 0 else NEG_INF
        a_right = A[i]     if i < m else POS_INF
        b_left  = B[j - 1] if j > 0 else NEG_INF
        b_right = B[j]     if j < n else POS_INF

        # Found correct partition
        if a_left <= b_right and b_left <= a_right:
            if total % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2.0

        # Move partition in A
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1

    # Given constraints guarantee a solution
    raise ValueError("Invalid input")

# O(log(m+n)) - Time complexity
# O(1) - Space complexity

print(find_median_sorted_arrays([1,3], [2])) # 2.0
print(find_median_sorted_arrays([1,2], [3, 4])) # 2.50
