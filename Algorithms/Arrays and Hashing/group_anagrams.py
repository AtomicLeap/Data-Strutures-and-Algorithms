# Leetcode 49. Group Anagrams

# https://leetcode.com/problems/group-anagrams/description/

from collections import defaultdict

# Use a character count tuple of length 26 (since only lowercase letters)
def group_anagrams(strs: list[str]) -> list[str]:
    group = defaultdict(list)

    for word in strs:
        count = [0] * 26 # Prefix list for all alphabets

        for char in word:
            count[ord(char) - ord('a')] += 1

        key = tuple(count) # tuples are hashable
        group[key].append(word)

    return list(group.values())

# N = number of strings, L = max length of string
# Time complexity: O(N·L)
# Space complexity: O(N·L) (for storing groups and hash keys).

print(group_anagrams(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams([""])) # [['']]
print(group_anagrams(["a"])) # [['a']]
print(group_anagrams([])) # []


# Sort the string (O(L log L) per string, where L = string length).
from collections import defaultdict

def group_anagrams_s(strs: list[str]) -> list[str]:
    groups = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))   # sorted string as key
        groups[key].append(word)
    
    return list(groups.values())

# N = number of strings, L = max length of string
# Time complexity: O(N·L logL) -> each string of length L is sorted.
# Space complexity: O(N·L) (for storing groups and hash keys).

print(group_anagrams_s(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(group_anagrams_s([""])) # [['']]
print(group_anagrams_s(["a"])) # [['a']]
print(group_anagrams_s([])) # []
