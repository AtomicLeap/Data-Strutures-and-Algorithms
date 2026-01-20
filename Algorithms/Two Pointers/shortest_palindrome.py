# Leetcode 214. Shortest Palindrome

# https://leetcode.com/problems/shortest-palindrome/description/

# Idea - Uses concept of Prefix-Suffix Match -> (KMP / Prefix Function)
"""
A prefix-suffix match of a string is a substring that is:
1. A prefix of the string -> (i.e., it starts at index 0)
2. AND also a suffix of the string -> (i.e., it ends at the last index)
3. But it cannot be equal to the entire string.

In short:

A prefix-suffix match is a substring that appears both at the beginning and 
at the end of the string.
"""

def shortest_palindrome(s: str) -> str:
    if not s:
        return s
    
    rev = s[::-1]
    # Build the combined string: original + '#' + reversed
    t = s + '#' + rev
    n = len(t)
    
    # Compute Longest Prefix-Suffix (LPS) match array for t
    longest_prefix_suffix_match = [0] * n
    
    # length of the current longest prefix-suffix
    length = 0
    
    # We start from i = 1 because longest_prefix_suffix_match[0] is always 0
    for i in range(1, n):
        # Move length back while we don't have a match
        while length > 0 and t[i] != t[length]:
            length = longest_prefix_suffix_match[length - 1]
        
        # If characters match, extend the current prefix-suffix
        if t[i] == t[length]:
            length += 1
            longest_prefix_suffix_match[i] = length
        # else longest_prefix_suffix_match[i] stays 0
    
    # longest_prefix_suffix_match[-1] is the length of the longest prefix of s that is a palindrome
    longest_pref_suffix_match = longest_prefix_suffix_match[-1]
    
    # Characters after this prefix suffix match need to be mirrored in front
    suffix_to_add = s[longest_pref_suffix_match:]
    
    # Reverse suffix_to_add and concat with string
    return suffix_to_add[::-1] + s

# O(n) - Time complexity
# O(n) - Space complexity -> extra space from slicing

print(shortest_palindrome("aacecaaa")) # "aaacecaaa"
print(shortest_palindrome("abcd")) # "dcbabcd"