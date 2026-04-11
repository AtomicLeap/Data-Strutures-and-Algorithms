# Leetcode 204. Count Primes

# https://leetcode.com/problems/count-primes/description/

# Tags -> Math, Enumeration, NumberTheory

#Idea: Use Sieve of Eratosthenes
"""
A number is prime if it has no divisors other than 1 and itself. 
Instead of checking every number individually, we mark multiples of each 
prime as non-prime.
"""

def count_primes(n: int) -> int:
    if n < 2:
        return 0
    
    is_prime_table = [True] * n
    is_prime_table[0] = is_prime_table[1] = False
    
    for num in range(2, int(n**0.5) + 1):
        if is_prime_table[num]:
            for number in range(num * num, n, num):
                is_prime_table[number] = False
    
    return sum(is_prime_table)

# O(n log log n) - Time complexity
# O(n) - Space complexity

print(count_primes(10)) # 4
print(count_primes(0)) # 0
print(count_primes(1)) # 0
print(count_primes(2)) # 0
