# Leetcode 208. Implement Trie (Prefix Tree)

# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class TrieNode:
    def __init__(self):
        self.children = {} # 26 letters of alphabets
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word_end = True

    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_word_end
        
    def starts_with(self, prefix: str) -> bool:
        current = self.root

        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True