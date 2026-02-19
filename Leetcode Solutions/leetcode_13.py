# Leetcode 13. Roman to Integer

# https://leetcode.com/problems/roman-to-integer/description/

def solution(s: str) -> int:
    n = len(s)
    result = 0
    roman_converter = { 
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
    
    for i in range(n - 1):
        curr_num = roman_converter[s[i]]
        next_num = roman_converter[s[i + 1]]
        if next_num > curr_num:
            result -= curr_num
        else:
            result += curr_num
    result += roman_converter[s[-1]]
    return result

# O(n) - Time complexity
# O(n) - Space complexity

print(solution("V"))
print(solution("III"))
print(solution("LVIII"))
print(solution("MCMXCIV"))