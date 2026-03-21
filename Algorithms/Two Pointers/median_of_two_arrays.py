# Leetcode 4. Median of Two Sorted Arrays

# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Two Pointer Solution 
# O(m + n)/2 ~ O(n) Worst case

def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    total = n1 + n2

    i = j = 0
    prev = curr = 0

    for _ in range(total // 2 + 1):
        prev = curr

        if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
            curr = nums1[i]
            i += 1
        else:
            curr = nums2[j]
            j += 1

    if total % 2 == 1:
        return float(curr)
    return (prev + curr) / 2.0

print(find_median_sorted_arrays([1, 12, 15, 16, 38], [2, 13, 17, 30, 45, 60])) # 16
print(find_median_sorted_arrays([1,3], [2])) # 2.0
print(find_median_sorted_arrays([1,2], [3,4])) # 2.5

            
        








