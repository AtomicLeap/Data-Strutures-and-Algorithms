# Leetcode 1545. Find Kth Bit in Nth Binary String

# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

# Tags -> String, Recursion

def find_kth_bit(n: int, k: int) -> str:
    flip = 0  # 0 = no flip, 1 = flipped odd number of times

    while n > 1:
        mid = 1 << (n - 1)      # 2^(n-1)
        if k == mid:
            return '0' if flip else '1'
        if k > mid:
            # map to mirrored position in S_{n-1} and toggle flip
            k = (1 << n) - k    # 2^n - k
            flip ^= 1
        n -= 1

    # S1 = "0"
    return '1' if flip else '0'

# O(k) - Time complexity
# O(1) - Space complexity

print(find_kth_bit(3, 1)) # 0
print(find_kth_bit(4, 11)) # 1
