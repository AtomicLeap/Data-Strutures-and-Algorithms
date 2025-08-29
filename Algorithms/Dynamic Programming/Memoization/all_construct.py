# all construct problem

"""
Write a function "all_construct(target, word_bank)" that takes a target 
and an array of strings as arguements. The function should return a 2D 
array containing all the ways the target can be constructed by concatenating 
elements of the word_bank array.

Constraints
You may reuse elements of the world_bank as many times as needed.
"""

# Brute force solution
def all_construct(target: str, word_bank: list[str]) -> list[list[str]] | list:
    if target == '':
        return [[]]
    
    total_construct = []
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            construct = all_construct(suffix, word_bank)
            total_construct += [[word, *item] for item in construct]
    return total_construct
    
# m = size of target
# n = len(word_bank)
# O(n^m) Time complexity
# O(m) Space complexity => max stack depth of m

# Optimized solution
def all_constructo(target: str, word_bank: list[str], memo: dict = {}) -> list[list[str]] | list:
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    
    total_construct = []
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            construct = all_constructo(suffix, word_bank, memo)
            total_construct += [[word, *item] for item in construct]
    memo[target] = total_construct
    return total_construct
# m = size of target
# n = len(word_bank)
# O(n^m) Time complexity
# O(m) Space complexity => max stack depth of m

print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef'])) # 3
print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar', 'e', 'a'])) # 3
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'abcd', 'purpl'])) # 2
print(all_construct('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # 1
print(all_construct('woman', ['w', 'cat', 'dog', 'def', 'man'])) # 0
print(all_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print('------------------------------------------')
# print(all_constructo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef'])) # 3
# print(all_constructo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar', 'e', 'a'])) # 3
# print(all_constructo('purple', ['purp', 'p', 'ur', 'le', 'abcd', 'purpl'])) # 2
# print(all_constructo('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # 1
# print(all_constructo('woman', ['w', 'cat', 'dog', 'def', 'man'])) # 0
# print(all_constructo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print(all_constructo('eeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
