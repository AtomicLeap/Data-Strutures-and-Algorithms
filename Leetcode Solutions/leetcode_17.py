# Leetcode 17. Letter Combinations of a Phone Number

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

# Tags -> Backtracking, String

def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []
    combination = []

    def backtrack(index: int):
        # base case: full combination built
        if index == len(digits):
            result.append("".join(combination))
            return

        letters = phone[digits[index]]

        for char in letters:
            combination.append(char)
            backtrack(index + 1)
            combination.pop()   # backtrack

    backtrack(0)
    return result

# Time complexity
# O(4^n) -> max = 4^4 = 256 combinations

# Space complexity
# O(n) recursion depth
# O(4^n) output

print(letter_combinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations("2")) # ["a","b","c"]