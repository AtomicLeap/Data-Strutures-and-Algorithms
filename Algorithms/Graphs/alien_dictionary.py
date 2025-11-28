# Leetcode 269. Alien Dictionary

# https://leetcode.com/problems/alien-dictionary/description/

from collections import defaultdict, deque
from typing import List

def alien_dict(words: List[str]) -> str:
    # Step A: initialize data structures
    adj = defaultdict(set)      # char -> set of chars that come after it
    indegree = {}               # char -> number of incoming edges
    
    # Put all unique characters into indegree with 0
    for word in words:
        for ch in word:
            indegree.setdefault(ch, 0)
    
    # Step B: build graph using pairwise comparisons
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        
        # Check the invalid prefix case: e.g., ["abc", "ab"]
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""
        
        # Find the first differing character
        min_len = min(len(w1), len(w2))
        for j in range(min_len):
            c1, c2 = w1[j], w2[j]
            if c1 != c2:
                # Edge c1 -> c2
                if c2 not in adj[c1]:   # avoid duplicating edge
                    adj[c1].add(c2)
                    indegree[c2] += 1
                break
        # If we never break (all chars same up to min_len),
        # we rely only on the prefix check above.

    # Step C: Kahn's algorithm for topological sort
    # Start with all chars of indegree 0
    queue = deque([ch for ch in indegree if indegree[ch] == 0])
    order = []
    
    while queue:
        ch = queue.popleft()
        order.append(ch)
        for nei in adj[ch]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    # If order doesn't contain all chars, there is a cycle
    if len(order) != len(indegree):
        return ""
    
    return "".join(order)


# C = number of distinct characters,
# N = number of words,
# L = total length of all words.

# Building graph: O(L) (comparing adjacent words).
# Topological sort: O(C + E) where E is edges, and E ≤ C², but in practice bounded by L.
# Overall: O(L + C + E) ≈ O(L) time, O(C + E) space.

# O(L) Time complexity
# O(C + E) Space complexity

print(alien_dict(["abc", "ab"])) # ""
print(alien_dict(["wrt", "wrf"])) # "wrtf"
print(alien_dict(["hrn","hrf","er","enn","rfnn"])) # "hernf"
print(alien_dict(["z","o"])) # "zo"