# Leetcode 273. Closest Prime Numbers in Range

# https://leetcode.com/problems/closest-prime-numbers-in-range/description/

# Tags -> Math, NumberTheory

# Use the Sieve of Eratosthenes
def closest_primes(left: int, right: int) -> list[int]:
    # Sieve of Eratosthenes
    def sieve_of_eratosthenes() -> list[int]:
        is_prime_table = [True] * (right + 1)
        if right >= 0:
            is_prime_table[0] = False
        if right >= 1:
            is_prime_table[1] = False

        num = 2
        while num * num <= right:
            if is_prime_table[num]:
                for multiple in range(num * num, right + 1, num):
                    is_prime_table[multiple] = False
            num += 1
        
        return [num for num in range(left, right + 1) if is_prime_table[num]]

    primes = sieve_of_eratosthenes()
    if len(primes) < 2:
        return [-1, -1]
    
    closest_pair = [primes[0], primes[1]]
    min_diff = primes[1] - primes[0]
    
    for i in range(2, len(primes)):
        diff = primes[i] - primes[i - 1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = [primes[i - 1], primes[i]]
    
    return closest_pair

# O(n log log n) - Time complexity, where n is the size of the range (right - left)
# O(n) - Space complexity, where n is the number of primes in the range

print(closest_primes(10, 19)) # [11, 13]
print(closest_primes(4, 6)) # [-1, -1]  
print(closest_primes(1, 10)) # [2, 3]
print(closest_primes(21, 25)) # [1-, -1]


# Use Range of Primality to find all primes in the given range
def closest_primes_r(left: int, right: int) -> list[int]: 
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    primes = [num for num in range(left, right + 1) if is_prime(num)]
    
    if len(primes) < 2:
        return [-1, -1]
    
    closest_pair = [primes[0], primes[1]]
    min_diff = primes[1] - primes[0]
    
    for i in range(2, len(primes)):
        diff = primes[i] - primes[i - 1]
        if diff < min_diff:
            min_diff = diff
            closest_pair = [primes[i - 1], primes[i]]
    
    return closest_pair

# O(n * sqrt(n)) - Time complexity, where n is the size of the range (right - left)
# O(n) - Space complexity, where n is the number of primes in the range

print(closest_primes_r(10, 19)) # [11, 13]
print(closest_primes_r(4, 6)) # [-1, -1] 
print(closest_primes_r(1, 10)) # [2, 3]
print(closest_primes(21, 25)) # [1-, -1]
