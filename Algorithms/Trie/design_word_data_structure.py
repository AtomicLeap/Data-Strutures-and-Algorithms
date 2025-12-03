# Leetcode 211. Design Add and Search Words Data Structure

# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False


class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word_end = True

    def search(self, word: str) -> bool:
        def dfs_helper(idx: int, node: TrieNode):
            if idx == len(word):
                return node.is_word_end

            char = word[idx]

            if char != ".":
                child = node.children.get(char)
                if not child:
                    return False
                return dfs_helper(idx + 1, child)
            else:
                for child in node.children.values():
                    if dfs_helper(idx + 1, child):
                        return True
                return False

        return dfs_helper(0, self.root)
    
# L = Length of word
# O(L) Time complexity
# O(L) Space complexity

"""
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]
"""