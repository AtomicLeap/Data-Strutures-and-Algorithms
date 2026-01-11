# Leetcode 3798. Largest Even Number

# https://leetcode.com/problems/largest-even-number/description/

def largest_even_num(s: str) -> str:
    num = int(s)
    while num and num & 1:
        num //= 10
    return str(num) if num else ""

# O(log n) - Time complexity
# O(1) - Space complexity

print(largest_even_num("1112")) # "1112"
print(largest_even_num("221")) # "22"
print(largest_even_num("1")) # ""
