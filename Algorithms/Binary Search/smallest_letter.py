# Leetcode 744. Find Smallest Letter Greater Than Target

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def smallest_letter(letters: list[str], target: str) -> str:
    n = len(letters)
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return letters[left % n]

# O(log n) - Time complexity
# O(1) - Space complexity
        

print(smallest_letter(["c","f","j"], "a")) # 'c'
print(smallest_letter(["c","f","j"], "c")) # 'f'
print(smallest_letter(["x","x","y","y"], "z")) # 'x'