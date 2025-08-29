# can construct problem

"""
Write a function "can_construct(target, word_bank)" that takes a target 
and an array of strings as arguements. The function should return a 
boolean indicating whether or not the target can be constructed
by concatenating elements of the word_bank array.

Constraints
You may reuse elements of the world_bank as many times as needed.
"""

# Brute force solution
def can_construct(target: str, word_bank: list[str]) -> bool:
    if target == '':
        return True
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, word_bank):
                return True
    return False
# m = size of target
# n = len(word_bank)
# O(n^m) Time complexity
# O(m ^ 2) Space complexity => max stack depth of m * size of suffix array m

# Optimized solution
def can_constructo(target: str, word_bank: list[str], memo: dict = {}) -> bool:
    if target in memo:
        return memo[target]
    if target == '':
        return True
    
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_constructo(suffix, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False
    return False
# m = size of target
# n = len(word_bank)
# O(m * n) Time complexity
# O(m * m) Space complexity

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('', ['ab', 'cat', 'dog', 'def', 'mouse']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))

print(can_constructo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))