# Leetcode 744. Find Smallest Letter Greater Than Target

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def next_greatest_letter(letters: list[str], target: str) -> str:
    ord_target = ord(target) - ord('a')
    min_letter_ord = -1
    for char in letters:
        ord_val = ord(char) - ord('a')
        if ord_val > ord_target:
            if min_letter_ord < 0:
                min_letter_ord = ord_val
            else:
                min_letter_ord = min(min_letter_ord, ord_val)
    return letters[0] if min_letter_ord < 0 else chr(ord('a') + min_letter_ord)
            
# O(n) - Time complexity
# O(1) - Space complexity


def smallest_letter(letters: list[str], target: str) -> str:
    n = len(letters)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    print(left)
    return letters[left % n]

# O(log n) - Time complexity
# O(1) - Space complexity

print(next_greatest_letter(["c","f","j"], "a")) # c
print(next_greatest_letter(["c","f","j"], "c")) # f
print(next_greatest_letter(["x","x","y","y"], "z")) # x

print(smallest_letter(["c","f","j"], "a")) # c
print(smallest_letter(["c","f","j"], "c")) # f
print(smallest_letter(["x","x","y","y"], "z")) # x