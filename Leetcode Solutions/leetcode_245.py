# Leetcode 245. Shortest Word Distance III

# https://leetcode.com/problems/shortest-word-distance-iii/description

# Tags -> Array, String

from math import inf

def shortest_word_distance(words_dict: list[str], word1: str, word2: str) -> int:
    shortest_dist = inf

    # Case 1: word1 and word2 are the same
    if word1 == word2:
        prev = -1

        for i, word in enumerate(words_dict):
            if word == word1:
                if prev != -1:
                    shortest_dist = min(shortest_dist, i - prev)
                prev = i

        return shortest_dist

    # Case 2: word1 and word2 are different
    idx1 = -1
    idx2 = -1

    for i, word in enumerate(words_dict):
        if word == word1:
            idx1 = i
        elif word == word2:
            idx2 = i

        if idx1 != -1 and idx2 != -1:
            shortest_dist = min(shortest_dist, abs(idx1 - idx2))

    return shortest_dist

# O(n) Time complexity
# O(1) Space complexity

print(shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")) # 1
print(shortest_word_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "makes")) # 3
