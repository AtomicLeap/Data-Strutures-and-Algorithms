# Leetcode 642 Design Search AutoComplete System

# https://leetcode.com/problems/design-search-autocomplete-system/description/


from typing import List, Dict

class TrieNode:
    def __init__(self):
        # Map character -> next TrieNode
        self.children: Dict[str, TrieNode] = {}
        # Map sentence -> frequency (for all sentences with prefix to this node)
        self.counts: Dict[str, int] = {}


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.current_input = ""   # what the user has typed in *this* session (since last '#')
        
        # Initialize the Trie with given sentences and frequencies
        for sentence, freq in zip(sentences, times):
            self._insert(sentence, freq)

    def _insert(self, sentence: str, freq: int) -> None:
        """
        Insert (or update) a sentence into the Trie with frequency increment `freq`.
        At each node along the path, we add `freq` to that sentence's count.
        """
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            # Update this node's counts for the sentence
            node.counts[sentence] = node.counts.get(sentence, 0) + freq

    def _search_prefix_node(self, prefix: str) -> TrieNode | None:
        """
        Walk down the Trie following the given prefix and return the final node.
        Return None if the prefix does not exist in the Trie.
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def _top_3(self, node: TrieNode) -> List[str]:
        """
        From this node's counts, return up to the top 3 sentences sorted by
        - highest frequency (descending)
        - then lexicographically (ASCII order) for ties
        """
        # node.counts: sentence -> freq
        items = list(node.counts.items())
        # Sort by (-freq, sentence) to meet rules
        items.sort(key=lambda x: (-x[1], x[0]))
        return [sentence for sentence, _ in items[:3]]

    def input(self, c: str) -> List[str]:
        """
        Handle a character being typed by the user.
        - If c == '#': finish the sentence, store it, reset buffer, and return [].
        - Otherwise: append to current_input, find top 3 suggestions for this prefix.
        """
        # Special end-of-sentence character
        if c == '#':
            # Store/update this complete sentence with +1 frequency
            if self.current_input:
                self._insert(self.current_input, 1)
            # Reset current prefix
            self.current_input = ""
            return []

        # Normal character: extend current prefix
        self.current_input += c

        # Find the node for this prefix
        node = self._search_prefix_node(self.current_input)
        if node is None:
            # No sentence with this prefix
            return []

        # Return top 3 hot sentences for this prefix
        return self._top_3(node)


# Time complexity
"""
L - the length of the sentence/prefix.
S = the number of distinct sentences stored.
"""

# Insert (_insert):
"""
We traverse characters of sentence: O(L).
At each node we update a dict entry: O(1) average.
So: O(L) per insert.
"""

# Input (input):
"""
For a normal character:
1. Append to current_input: O(1).
2. '_search_prefix_node' walks down at most L nodes: O(L).
3. '_top_3' sorts up to S_prefix sentences under that node.
    Sorting: O(S_prefix log S_prefix) worst case.

Under constraints (n <= 100 initial, <= 5000 calls, sentence lengths ≤ 200), 
this is perfectly fine.
"""

# Space complexity
"""
At most one node per character per sentence: O(total_chars).
Each node’s counts may include many sentences, but with constraints it remains 
manageable: O(S * avg_sentence_length) overall.
"""