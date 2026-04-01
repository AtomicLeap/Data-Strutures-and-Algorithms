# Leetcode 243. Shortest Word Distance

# https://leetcode.com/problems/shortest-word-distance/description

# Tags -> Array, String

def shortest_distance(words: list[str], word1: str, word2: str) -> int:
    index1, index2 = -1, -1
    min_distance = float('inf')

    for i, word in enumerate(words):
        if word == word1:
            index1 = i
        elif word == word2:
            index2 = i

        if index1 != -1 and index2 != -1:
            min_distance = min(min_distance, abs(index1 - index2))

    return min_distance

# O(n) Time complexity
# O(1) Space complexity

print(shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")) # 3
print(shortest_distance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")) # 1
