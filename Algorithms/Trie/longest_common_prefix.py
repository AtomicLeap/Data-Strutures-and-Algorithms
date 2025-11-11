# Leetcode 14. Longest Common Prefix

# https://leetcode.com/problems/longest-common-prefix/

# Idea

"""
1. Insert all strings into a Trie.
2. Starting from the root, keep walking down as long as:
    - the current node has exactly one child, and
    - the current node is not the end of a word.
3. The path you walked (characters collected) is the LCP.
    If any string is empty, the LCP is "".

This works because a common prefix is exactly the part of the tree before 
any branching or word-end.
"""

class TrieNode:
    __slots__ = ("children", "is_word")
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.is_word = False   # marks end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def longest_common_prefix(self) -> str:
        node = self.root
        prefix_chars = []

        # walk while: single child AND not at a completed word
        while not node.is_word and len(node.children) == 1:
            [char] = node.children.keys()
            prefix_chars.append(char)
            node = node.children[char]

        return "".join(prefix_chars)

def longest_common_prefix(strs):
    if not strs:
        return ""
    # if any string is empty, LCP is empty
    if any(len(s) == 0 for s in strs):
        return ""

    trie = Trie()
    for s in strs:
        trie.insert(s)
    return trie.longest_common_prefix()

print(longest_common_prefix(["flower","flow","flight"])) # "fl"
print(longest_common_prefix(["dog","racecar","car"])) # " "
print(longest_common_prefix(["dogeman","doge","dogey"])) # "doge"