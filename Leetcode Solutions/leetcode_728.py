# Leetcode 728. Self Dividing Numbers

# https://leetcode.com/problems/self-dividing-numbers/description/

# Tags -> Math

def self_dividing_numbers(left: int, right: int) -> list[int]:
    def is_self_dividing(num: int) -> bool:
        number = num

        while number > 0:
            digit = number % 10
            if digit == 0 or num % digit != 0:
                return False
            number //= 10
        return True

    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)

    return result

# O(n * d) Time complexity, where n is the range of numbers and
#           d is the number of digits in the largest number
# O(n) Space complexity

print(self_dividing_numbers(1, 22)) # [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(self_dividing_numbers(47, 85)) # [48,55,66,77]
print(self_dividing_numbers(1, 100)) # [1,2,3,4,5,6,7,8,9,11,12,15,22,24,33,36,44,48,55,66,77,88,99]    


def self_dividing_numbers_s(left: int, right: int) -> list[int]:
    def is_self_dividing(num: int) -> bool:
        for digit in str(num):
            if digit == '0' or num % int(digit) != 0:
                return False
        return True

    result = []
    for num in range(left, right + 1):
        if is_self_dividing(num):
            result.append(num)

    return result

# O(n * d) Time complexity, where n is the range of numbers and 
#           d is the number of digits in the largest number
# O(n) Space complexity

print(self_dividing_numbers_s(1, 22)) # [1,2,3,4,5,6,7,8,9,11,12,15,22]
print(self_dividing_numbers_s(47, 85)) # [48,55,66,77]
print(self_dividing_numbers_s(1, 100)) # [1,2,3,4,5,6,7,8,9,11,12,15,22,24,33,36,44,48,55,66,77,88,99]
