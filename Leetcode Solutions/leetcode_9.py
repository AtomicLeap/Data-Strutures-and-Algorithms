# Leetcode 9. Palindrome Number

# https://leetcode.com/problems/palindrome-number/description/

def solution_1(num: int) -> bool:
  num_str = str(num)
  n = len(num_str)
  for i in range(n // 2):
    if num_str[i] != num_str[n - i - 1]:
      return False
  return True

# O(n/2) ~ O(n) - Time complexity
# O(1) - Space complexity

def solution_2(num: int) -> bool:
  num_str = str(num)
  
  return num_str == num_str[::-1]

# O(n) - Time complexity
# O(1) - Space complexity

# More Efficient solution
def solution_3(num: int) -> bool:
    # Negative numbers or numbers ending with 0 (but not 0 itself) are not palindromes
    if num < 0 or (num % 10 == 0 and num != 0):
        return False

    reversed_half = 0
    while num > reversed_half:
        reversed_half = reversed_half * 10 + num % 10
        num //= 10

    # For even-length numbers: num == reversed_half
    # For odd-length numbers: num == reversed_half // 10 (middle digit ignored)
    return num == reversed_half or num == reversed_half // 10

# O(n.log n) - Time complexity
# O(1) - Space complexity

print(solution_3(121))
print(solution_3(-121))
print(solution_3(10))
print(solution_3(0))
print(solution_3(5))
print(solution_3(1000))