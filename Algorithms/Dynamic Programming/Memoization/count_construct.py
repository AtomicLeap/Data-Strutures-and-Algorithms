# count construct problem

"""
Write a function "count_construct(target, word_bank)" that takes a target 
and an array of strings as arguements. The function should return the 
total number of ways the target can be constructed by concatenating 
elements of the word_bank array.

Constraints
You may reuse elements of the world_bank as many times as needed.
"""

# Brute force solution
def count_construct(target: str, word_bank: list[str]) -> int:
    if target == '':
        return 1
    
    total_ways = 0
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways = count_construct(suffix, word_bank)
            total_ways += num_ways
    return total_ways
    
# m = size of target
# n = len(word_bank)
# O(n^m) Time complexity
# O(m ^ 2) Space complexity => max stack depth of m * size of suffix array m

# Optimized solution
def count_constructo(target: str, word_bank: list[str], memo: dict = {}) -> int:
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    
    total_ways = 0
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways = count_constructo(suffix, word_bank, memo)
            total_ways += num_ways
    memo[target] = total_ways
    return total_ways
# m = size of target
# n = len(word_bank)
# O(m * n) Time complexity
# O(m * m) Space complexity

print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef'])) # 3
print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar', 'e', 'a'])) # 3
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'abcd', 'purpl'])) # 2
print(count_construct('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # 1
print(count_construct('woman', ['w', 'cat', 'dog', 'def', 'man'])) # 0
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print('------------------------------------------')
# print(count_constructo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef'])) # 3
# print(count_constructo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar', 'e', 'a'])) # 3
# print(count_constructo('purple', ['purp', 'p', 'ur', 'le', 'abcd', 'purpl'])) # 2
# print(count_constructo('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # 1
# print(count_constructo('woman', ['w', 'cat', 'dog', 'def', 'man'])) # 0
# print(count_constructo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # 4
print(count_constructo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
