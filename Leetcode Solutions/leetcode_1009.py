# Leetcode 1009. Complement of Base 10 Integer

# https://leetcode.com/problems/complement-of-base-10-integer/description/

# Tags -> Bit manipulation

def bitwise_complement(n: int) -> int:
    if n == 0:
        return 1
    
    # mask = (1 << k) - 1, where k = len(bin(n))
    mask = (1 << n.bit_length()) - 1
    return mask ^ n

# O(1) - Time complexity
# O(1) - Space complexity

print(bitwise_complement(5)) # 2
print(bitwise_complement(7)) # 0
print(bitwise_complement(10)) # 5
