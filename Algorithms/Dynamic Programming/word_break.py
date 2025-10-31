# Leetcode 139. Word Break

# https://leetcode.com/problems/word-break/description/

# Idea
# Lets assume we are joining words of the wordDict to form the string s.
# If it is possible to join words from wordDict to form string s, then return True.

# Iterative solution (tabulation)
def break_word(s: str, word_dict: list[str]) -> bool:
    n = len(s)
    table = [False for _ in range(n + 1)]
    table[0] = True

    for i in range(n + 1):
        if table[i]:
            for word in word_dict:
                m = len(word)
                if s[i: i + m] == word and i + m < n + 1:
                    table[i + m] = True
    return table[n]

# m = len(s), n = len(word_dict)
# O(m * n) Time complexity
# O(m) Space complexity

print(break_word("leetcode", ["leet","code"])) # True
print(break_word("applepenapple", ["apple","pen"])) # True
print(break_word("catsandog", ["cats","dog","sand","and","cat"])) # False 
