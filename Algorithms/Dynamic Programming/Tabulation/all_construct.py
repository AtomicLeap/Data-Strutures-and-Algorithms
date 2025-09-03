# all construct problem

# Write a function "all_construct(target, word_bank)" that takes a target 
# and an array of strings as arguements. The function should return a 2D 
# array containing all the ways the target can be constructed by concatenating 
# elements of the word_bank array.

# Constraints
# You may reuse elements of the world_bank as many times as needed.

# Tabulation solution
def all_construct(target: str, word_bank: list[str]) -> list[list[str]] | list:
    n = len(target)
    table = [[] for _ in range(n + 1)]
    table[0] = [[]] # Ways to generate an empty string

    for i in range(n + 1):
        if table[i]:
            for word in word_bank:
                word_size = len(word)
                if word == target[i : i + word_size]:
                    combination = [[*sub_array, word] for sub_array in table[i]]
                    table[i + word_size] += combination
    return table[n]

# m = size of target
# n = len(numbers)
# O(n ^ m) Time complexity => Exponential time
# O(n * m) Space complexity => Exponential space

print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef'])) # 3 [['ab', 'cd', 'ef'], ['abcd', 'ef'] ['abc', 'def']]
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar', 'e', 'a'])) # 3
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'abcd', 'purpl'])) # 2
print(all_construct('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # 1
print(all_construct('woman', ['w', 'cat', 'dog', 'def', 'man'])) # 0
print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print(all_construct('eeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # 0
