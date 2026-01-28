# Leetcode 3813. Vowel-Consonant Score

def vowel_count(s: str) -> int:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_count = 0
    consonant_count = 0
    for char in s:
        if char in vowels:
            vowel_count += 1
        if char in consonants:
            consonant_count += 1
    return vowel_count // consonant_count if consonant_count else 0

# O(n) - Time omplexity
# O(1) - Space omplexity

print(vowel_count('cooear')) # 2
print(vowel_count('axeyizou')) # 1
print(vowel_count('au 123')) # 0