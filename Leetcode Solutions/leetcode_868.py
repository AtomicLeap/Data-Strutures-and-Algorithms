# Leetcode 868. Binary Gap

# https://leetcode.com/problems/binary-gap/description

# Tags -> Bit Manipulation

def binary_gap(n: int) -> int:
    bin_num = bin(n)[2:]   # remove "0b"
    max_gap = 0
    last_idx = -1

    for idx, char in enumerate(bin_num):
        if char == '1':
            if last_idx != -1:
                max_gap = max(max_gap, idx - last_idx)
            last_idx = idx

    return max_gap

# O(log n) - Time complexity
# O(log n) - Space complexity -> binary string storage

# Optimal solution
def binary_gap_i(n: int) -> int:
    max_gap = 0
    prev = -1          # position of the previous 1-bit
    pos = 0            # current bit position (0 = LSB)

    while n > 0:
        if n & 1:
            if prev != -1:
                max_gap = max(max_gap, pos - prev)
            prev = pos
        n >>= 1
        pos += 1

    return max_gap

# O(log n) - Time complexity
# O(1) - Space complexity

print(binary_gap(22)) # 2
print(binary_gap(8)) # 0
print(binary_gap(5)) # 2
