# Leetcode 389. Find the Difference

# https://leetcode.com/problems/find-the-difference/description/

# XOR trick
def find_difference(s: str, t: str) -> str:
    diff = 0 # Zero is Identity for XOR

    for char in s:
        diff ^= ord(char)

    for char in t:
        diff ^= ord(char)

    return chr(diff)

# O(n) Time complexity
# O(1) Space complexity

print(find_difference('abcd', 'adecb')) # 'e'
print(find_difference('', 'y')) # 'y'

# Tabulation - Since we are only concerned with alphabets
def find_difference_t(s: str, t: str) -> str:
    table = [0] * 26

    for char in t:
        table[ord(char) - ord('a')] += 1
    
    for char in s:
        table[ord(char) - ord('a')] -= 1
    
    for idx, value in enumerate(table):
        if value == 1:
            return chr(idx + ord('a'))
        
# O(n) Time complexity
# O(1) Space complexity

print(find_difference_t('abcd', 'adecb')) # 'e'
print(find_difference_t('', 'y')) # 'y'