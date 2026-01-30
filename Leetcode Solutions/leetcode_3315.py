# Leetcode 3315. Construct the Minimum Bitwise Array II

# https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/description

def min_bitwise_array(nums: list[int]) -> list[int]:
    results = []
    for y in nums:
        if (y & 1) == 0:  # even -> cannot end with trailing 1s
            results.append(-1)
            continue

        k = 0
        tmp = y
        while tmp & 1:      # count trailing 1s
            k += 1
            tmp >>= 1

        results.append(y - (1 << (k - 1)))
    return results


# O(n * log(max(nums))) (≤ 100 * 30) - Time complexity
# O(1) - Space complexity

print(min_bitwise_array([2,3,5,7])) # [-1,1,4,3]
print(min_bitwise_array([11,13,31])) # [9,12,15]
