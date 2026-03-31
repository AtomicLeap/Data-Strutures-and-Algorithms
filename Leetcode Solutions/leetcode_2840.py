# Leetcode 2840. Check if Strings Can be Made Equal With Operations II

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description

# Tags -> String, Sorting

def can_be_equal(s1: str, s2: str) -> bool:
    even1 = [0] * 26
    odd1 = [0] * 26
    even2 = [0] * 26
    odd2 = [0] * 26

    for i, ch in enumerate(s1):
        idx = ord(ch) - ord('a')
        if i % 2 == 0:
            even1[idx] += 1
        else:
            odd1[idx] += 1

    for i, ch in enumerate(s2):
        idx = ord(ch) - ord('a')
        if i % 2 == 0:
            even2[idx] += 1
        else:
            odd2[idx] += 1

    return even1 == even2 and odd1 == odd2

# O(n) Time complexity
# O(1) Space complexity

print(can_be_equal("abcdba", "cabdab")) # True
print(can_be_equal("abe", "bea")) # False

def can_be_equal_o(s1: str, s2: str) -> bool:
    even = [0] * 26
    odd = [0] * 26

    for i in range(len(s1)):
        if i % 2 == 0:
            even[ord(s1[i]) - ord('a')] += 1
            even[ord(s2[i]) - ord('a')] -= 1
        else:
            odd[ord(s1[i]) - ord('a')] += 1
            odd[ord(s2[i]) - ord('a')] -= 1

    return all(x == 0 for x in even) and all(x == 0 for x in odd)

# O(n) Time complexity
# O(1) Space complexity

print(can_be_equal("abcdba", "cabdab")) # True
print(can_be_equal("abe", "bea")) # False

from collections import Counter
def can_be_equal_e(s1: str, s2: str) -> bool:
    return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])

# O(n) Time complexity
# O(1) Space complexity

print(can_be_equal_e("abcdba", "cabdab")) # True
print(can_be_equal_e("abe", "bea")) # False