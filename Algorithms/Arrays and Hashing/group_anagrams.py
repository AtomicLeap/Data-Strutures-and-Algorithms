# Leetcode 49. Group Anagrams

"""
Given an array of strings strs, group the anagrams together. You can return the
 answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict

# Use a character count tuple of length 26 (since only lowercase letters)
def group_anagrams(strs: list[str]) -> list[str]:
    group = defaultdict(list)

    for word in strs:
        count = [0] * 26 # Prefix list for all alphabets

        for char in word:
            count[ord(char) - ord('a')] += 1

        key = tuple(count) # turples are hashable
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
