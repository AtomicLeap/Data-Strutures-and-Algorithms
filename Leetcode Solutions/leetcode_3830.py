# Leetcode 3830. Longest Alternating Subarray After Removing At Most One Element

# https://leetcode.com/problems/longest-alternating-subarray-after-removing-at-most-one-element/description/

def max_alternating_subarray_length(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0

    # dp ending at i-1
    up0 = down0 = 1
    up1 = down1 = 1

    # dp ending at i-2 (needed to "skip i-1")
    up0_i2 = down0_i2 = 1

    results = 1

    for i in range(1, n):
        a, b = nums[i - 1], nums[i]

        # --- no deletion ---
        if a < b:
            new_up0 = down0 + 1
            new_down0 = 1
        elif a > b:
            new_down0 = up0 + 1
            new_up0 = 1
        else:
            new_up0 = new_down0 = 1  # strict alternation breaks on equality

        # --- one deletion ---
        # Option 1: already used deletion somewhere earlier, extend with i-1 -> i
        cand_up1 = (down1 + 1) if a < b else 1
        cand_down1 = (up1 + 1) if a > b else 1

        # Option 2: use deletion now by deleting nums[i-1], connect nums[i-2] -> nums[i]
        if i >= 2:
            c = nums[i - 2]
            if c < b:
                cand_up1 = max(cand_up1, down0_i2 + 1)
            if c > b:
                cand_down1 = max(cand_down1, up0_i2 + 1)

        new_up1 = max(1, cand_up1)
        new_down1 = max(1, cand_down1)

        results = max(results, new_up0, new_down0, new_up1, new_down1)

        # shift (i-2) <- (i-1), (i-1) <- (i)
        up0_i2, down0_i2 = up0, down0
        up0, down0 = new_up0, new_down0
        up1, down1 = new_up1, new_down1

    return results

# O(n) - Time complexity
# O(1) - Space complexity

print(max_alternating_subarray_length([2,1,3,2])) # 4
print(max_alternating_subarray_length([3,2,1,2,3,2,1])) # 4
print(max_alternating_subarray_length([100000,100000])) # 1