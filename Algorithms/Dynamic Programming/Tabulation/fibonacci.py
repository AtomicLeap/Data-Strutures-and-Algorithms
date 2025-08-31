# nth Fibonacci number
# get the nth fibonacci number

# Tabulation solution
def fib(n: int)-> int:
    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]

# O(n) Time complexity
# O(n) Space complexity


print(fib(5)) # 5
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025