# 476. Number Complement

# https://leetcode.com/problems/number-complement/description/

# Tags -> Bit manipulation

def find_complement(num: int) -> int:
    if num == 0:
        return 1
    
    # mask = (1 << k) - 1, where k = len(bin(n))
    mask = (1 << num.bit_length()) - 1
    return mask ^ num

# O(1) - Time complexity
# O(1) - Space complexity

print(find_complement(5)) # 2
print(find_complement(7)) # 0
print(find_complement(10)) # 5
