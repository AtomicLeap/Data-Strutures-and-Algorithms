# nth Fibonacci number
# get the nth fibonacci number

# Brute force solution
def fib(n: int)-> int:
    if n <= 2: #base case
        return 1
    return fib(n - 1) + fib(n - 2)
# O(2^n) Time complexity = > 2 recursive calls
# O(n) Space complexity => max stack depth of n

# Optimized solution
def fibo(n: int, memo: dict = {}) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibo(n - 1, memo) + fibo(n - 2, memo)
    return memo[n]
# O(n) Time complexity = > memoization with dictionary
# O(n) Space complexity => max stack depth of n


print(fib(5)) # 5
print(fib(7)) # 13
print(fib(8)) # 21
print(fibo(5)) # 5
print(fibo(7)) # 13
print(fibo(8)) # 21
print(fibo(50)) # 12586269025