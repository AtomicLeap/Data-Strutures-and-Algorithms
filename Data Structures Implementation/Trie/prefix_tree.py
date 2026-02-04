# Leetcode 208. Implement Trie (Prefix Tree)

# https://leetcode.com/problems/implement-trie-prefix-tree/description/


# Use HashMap per Node

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

   
# Use Fixed 26-Array per Node

class TrieNodeA:
    def __init__(self):
        # Fixed array of 26 children
        self.children = [None] * 26
        self.is_word_end = False

class TrieA:
    def __init__(self):
        self.root = TrieNodeA()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not current.children[idx]:
                current.children[idx] = TrieA()
            current = current.children[idx]
        current.is_word_end = True
    
    def search(self, word: str) -> bool:
        current = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return current.is_word_end
    
    def starts_with(self, word: str) -> bool:
        current = self.root

        for char in word:
            idx = ord(char) - ord('a')
            if not current.children[idx]:
                return False
            current = current.children[idx]
        return True

