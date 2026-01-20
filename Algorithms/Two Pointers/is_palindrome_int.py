# Leetcode 9. Palindrome Number

# https://leetcode.com/problems/palindrome-number/description/

# 1) Palindrome check (integer, no strings)
def is_palindrome_int(x: int) -> bool:
    # negatives and numbers ending with 0 (but not 0 itself) can't be palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    rev = 0
    # reverse only half the digits
    while x > rev:
        rev = rev * 10 + (x % 10)   # take last digit
        x //= 10                    # drop last digit                  

    # For odd digit counts, rev has one extra middle digit → drop it with // 10
    return x == rev or x == rev // 10

# O(n / 2) - Time complexity
# O(1) - Space complexity

# 2) Palindrome check (convert int to strings)
def is_palindrome(x: int) -> bool:
    num_str = str(x)
    n = len(num_str)

    left = 0
    right = n - 1

    while left < right:
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1
    return True

    # Alternatively for Two pointers
    # for i in range(n // 2):
    #     if num_str[i] != num_str[n - 1 - i]:
    #         return False
    # return True

# O(n / 2) - Time complexity
# O(1) - Space complexity


# n = number of digits in number
# O(n) - Time complexity
# O(1) - Space complexity

print(is_palindrome_int(121)) # True
print(is_palindrome_int(1221)) # True
print(is_palindrome_int(-121)) # False
print(is_palindrome_int(10)) # False

print(is_palindrome(121)) # True
print(is_palindrome(1221)) # True
print(is_palindrome(-121)) # False
print(is_palindrome(10)) # False