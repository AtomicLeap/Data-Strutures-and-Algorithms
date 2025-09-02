# can construct problem

# Write a function "can_construct(target, word_bank)" that takes a target 
# and an array of strings as arguements. The function should return a 
# boolean indicating whether or not the target can be constructed
# by concatenating elements of the word_bank array.

# Constraints
# You may reuse elements of the world_bank as many times as needed.

# Tabulation solution
def can_construct(target: str, word_bank: list[str]) -> bool:
    n = len(target)
    table = [False for _ in range(n + 1)] # Table columns correspond to characters of target 
    table[0] = True # An empty string can be generated with any word_bank

    for i in range(n + 1):
        if table[i] == True:
            for word in word_bank:
                if word == target[i : i + len(word)]:
                    table[i + len(word)] = True
    return table[n]

# m = len(target)
# n = len(word_bank)
# O(n * m * m) Time complexity
# O(m) Space complexity => size of the table

print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])) # True
print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) # False
print(can_construct('', ['ab', 'cat', 'dog', 'def', 'mouse'])) # True
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't'])) # True
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee'])) # False