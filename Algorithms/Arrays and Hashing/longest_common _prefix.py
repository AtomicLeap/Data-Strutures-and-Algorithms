# Leetcode 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/description/

def longest_common_prefix(strs: list[str]) -> str:
    prefix_str = ""
    if not strs:
        return prefix_str
    
    for chars in zip(*strs):
        if len(set(chars)) > 1:
            break
        prefix_str += chars[0]
        
    return prefix_str

# O(n) Time complexity
# O(n) Space complexity

# Horizontal scanning 
def longest_common_prefix_h(strs):
    if not strs:
        return ""
    
    # Take the first string as initial prefix
    prefix = strs[0]
    
    for s in strs[1:]:
        # Reduce prefix until it fits
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            # If prefix becomes empty, return quickly
            if not prefix:
                return ""
    
    return prefix

# n = number of strings, m = length of shortest string.
# O(n . m) Time complexity
# O(n) Space complexity

print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(longest_common_prefix(["dog","racecar","car"])) # " "

print(longest_common_prefix_h(["flower","flow","flight"])) # "fl"
print(longest_common_prefix_h(["dog","racecar","car"])) # " "