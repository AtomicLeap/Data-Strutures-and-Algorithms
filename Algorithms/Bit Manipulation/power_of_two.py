# Leetcode 231. Power of Two

# https://leetcode.com/problems/power-of-two/description/

# Idea:
# A number that is a power of two, has only one bit set
# And such a number is only a positive integer (number > 0)
def is_power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0

print(is_power_of_two(1)) # 2^0 - True
print(is_power_of_two(16)) # 2^4 - True
print(is_power_of_two(3)) # False
print(is_power_of_two(0)) # False