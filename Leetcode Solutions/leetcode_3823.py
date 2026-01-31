# Leetcode 3823. Reverse Letters Then Special Characters in a String

# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/

def reverse_by_type(s: str) -> str:
    n = len(s)
    pref_list = [0] * n
    letters = ''
    special_chars = ''
    for i in range(n):
        if s[i].isalpha():
            letters += s[i]
            pref_list[i] = 1
        else:
            special_chars += s[i]
    letters = letters[::-1]
    special_chars = special_chars[::-1]
    idx_letters = 0
    idx_sp_chars = 0

    for i in range(n):
        if pref_list[i]:
            pref_list[i] = letters[idx_letters]
            idx_letters += 1
        else:
            pref_list[i] = special_chars[idx_sp_chars]
            idx_sp_chars += 1
    return ''.join(pref_list)

# O(n) - Time complexity
# O(n) - Space complexity

print(reverse_by_type(")ebc#da@f("))
print(reverse_by_type("z"))
print(reverse_by_type("!@#$%^&*()"))