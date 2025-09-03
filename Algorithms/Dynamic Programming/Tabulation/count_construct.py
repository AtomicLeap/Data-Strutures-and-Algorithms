# count construct problem

# Write a function "count_construct(target, word_bank)" that takes a target 
# and an array of strings as arguements. The function should return the 
# total number of ways the target can be constructed by concatenating 
# elements of the word_bank array.

# Constraints
# You may reuse elements of the world_bank as many times as needed.

# Tabulation solution
def count_construct(target: str, word_bank: list[str]) -> int:
    n = len(target)
    table = [0 for _ in range(n + 1)]  # Table columns correspond to characters of target 
    table[0] = 1 # Number of ways to generate an empty string

    for i in range(n + 1):
        if table[i]:
            for word in word_bank:
                word_size = len(word)
                if word == target[i : i + word_size]:
                    table[i + word_size] += table[i]
    return table[n]
    
# m = len(target)
# n = len(word_bank)
# O(n * m * m) Time complexity
# O(m) Space complexity => size of the table


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef'])) # 3
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar', 'e', 'a'])) # 3
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'abcd', 'purpl'])) # 2
print(count_construct('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # 1
print(count_construct('woman', ['w', 'cat', 'dog', 'def', 'man'])) # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # 0
