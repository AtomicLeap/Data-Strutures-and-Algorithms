# Leetcode 271 Encode and Decode Strings

"""
Design an algorithm to encode a list of strings into a single string. 
The encoded string should be able to be decoded back to the original list of strings 
(i.e., a reversible transformation).

You need to implement two functions/methods:
encode(strs: List[str]) -> str: Encodes a list of strings to a single string.
decode(s: str) -> List[str]: Decodes the single string back to the original list of strings.

Example 1
Input: ["leet","code","love","you"]
Output: ["leet","code","love","you"]

Example 2
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Clarifications & Constraints
The list of strings strs may be empty, or contain empty strings.
Each string may contain any possible characters, including letters, digits, symbols, 
any UTF-8 characters.
The operations of encode and decode must be reversible, i.e., decoding the encoded string 
of strs should return exactly strs.
Make sure your solution handles special characters properly (e.g. "#", spaces, etc.), 
not assuming any character won't appear in the strings.
You should aim for an efficient solution in terms of both time and space usage.
"""

class Codec:
    def encode(self, strs: list[str]) -> str:
        # length-in-characters + '#' + string
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> list[str]:
        res, i, n = [], 0, len(s)
        while i < n:
            # read length up to '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res

codec = Codec()

print(codec.encode(["leet","code","love","you"])) # 4#leet4#code4#love3#you
print(codec.encode(["we","say",":","yes"])) # 2#we3#say1#:3#yes
print(codec.decode('4#leet4#code4#love3#you')) # ["leet","code","love","you"]
print(codec.decode('2#we3#say1#:3#yes')) # ["we","say",":","yes"]
