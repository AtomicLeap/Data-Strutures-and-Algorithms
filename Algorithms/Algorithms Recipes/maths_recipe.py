# Maths Recipe

# 1. modulo (%) operator
# 2. floor division (//) operator
# 3. greatest common divisor (gcd)
# 4. Sum of first N numbers (1 to N)
# 5. Arithmetic Progression ->  a(n) = a(1) + (n - 1) * d
# 6. Sum of Arithmetic Progression -> S(n) = (n // 2)*(2*a + (n - 1)*d)
# 7. Geometric Progression -> a(n) = a * r ** (n - 1)
# 8. Sum of Geometric Progression -> S(n) = a * (r ** (n - 1) // (r - 1) for r != 1
#        if r == 1, S(n) = n * a
# 9. Sum of Powers of Two -> S(n) = 2 ** (n + 1) - 1
# 10. Permutation -> P(n, r) = n!//(n - r)!
# 11. Combination -> C(n, r) = n! // (r! * (n - r)!)


# 1. Modulo operator (%)

"""
Mathematical idea of modulo
Modulo is defined so that for any integers a and positive n:
    a % n = r <-> a = q.n + r,    where 0 <= r < n
q is an integer (the quotient)
r is the remainder

The key rule is that the remainder is always non-negative.
Example:
1. -1 % 4 = 3   -> -1 = (-1).4 + 3
2. -3 % 2 = 1   -> -3 = (-2).2 + 1

Returns the **remainder** after dividing one number by another.
a % b = remainder when a is divided by b

Example:
7 % 3  # = 1  (since 3*2 = 6, remainder = 1)

Key property:
a = (a // b) * b + (a % b)
"""
# 2. Floor division (//)

"""
Divides two numbers and **rounds down** to the nearest integer (toward negative infinity).
a // b = floor(a / b)

Example:
7 // 3  # = 2

Another example (with negatives):
-7 // 3  # = -3  (since floor(-2.333) = -3)
-7 % 3   # = 2   (since -7 = (-3)*3 + 2)

Practical Uses and Examples
Example 1: Extracting digits (used in math-based problems)

Suppose you need to 'reverse digits' of an integer `x = 1234`.
"""

rev = 0
num = 1234
while num > 0:
    last_digit = num % 10       # get last digit
    rev = rev * 10 + last_digit
    num //= 10             # remove last digit
print(rev)  # Output: 4321

"""
Why it works:
1. `% 10` isolates the last digit.
2. `// 10` removes the rest of the digits except the last.

Used in problems like:
* Reversing integers
* Palindrome numbers
* Counting digits
---

Example 2: Circular array / rotation

In a 'circular array', indices wrap around.
For example, moving 1 step forward from index `n-1` should go back to `0`.

"""
arr = [10, 20, 30, 40]
n = len(arr)
index = (3 + 1) % n   # move one step forward from last element
print(index)  # 0

"""
Why it works:
Modulo keeps index within bounds of `[0, n-1]`.

Used in:
* Rotating arrays
* Circular queues
* Hash tables (open addressing)
"""

# Example 3: Hash function in Hash Tables

key = 12345
table_size = 10
index = key % table_size

"""
Why it works:**
Modulo distributes keys evenly across slots `0..9`.

Used in:
* Hash maps
* Bloom filters
* Cuckoo hashing
---

Example 4: Even/Odd checking

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

Why it works:
Modulo quickly checks divisibility.

Used in:
* Bitmask problems
* Parity checks
* Alternating sequences
---

Example 5: Working with time or cycles

Problem: What time will it be 9 hours after 11 o'clock?
"""

time = (11 + 9) % 12
print(time)  # 8

"""
Why it works:
The modulo "wraps around" the 12-hour clock.
---

Example 6: Finding middle index (using floor division)

Used in .binary search' or 'merge sort'.
"""

low, high = 0, n - 1
mid = (low + high) // 2

"""
Why it works:**
`//` ensures an integer index (no float).

Used in:
* Binary Search
* Divide & Conquer algorithms
* Linked list splitting (slow/fast pointer)
---

Example 7: Modulo for repeating patterns
When something repeats every `k` steps — use `%`.

Example: cycle through colors every 3 elements.

colors = ["red", "green", "blue"]
for i in range(10):
    print(colors[i % 3])

Output cycles: red → green → blue → red → …
---

Example 8: Modular arithmetic (in big number problems)
Used in problems like:

* Large Fibonacci numbers
* Modular exponentiation
* Cryptography (RSA, etc.)


MOD = 1_000_000_007
result = (a + b) % MOD


Why it works:**
Keeps numbers small and prevents overflow.
---

4. Summary Table

| Operation           | Meaning                  | Example           | Common Use                             |
| ------------------- | ------------------------ | ----------------- | -------------------------------------- |
| `a % b`             | remainder of a ÷ b       | `10 % 3 = 1`      | wrap-around, hashing, digit extraction |
| `a // b`            | integer division (floor) | `10 // 3 = 3`     | midpoint, digit removal, loop steps    |
| `(i + 1) % n`       | circular next index      | `(3 + 1) % 4 = 0` | circular queue, rotation               |
| `x % 2`             | check even/odd           | `5 % 2 = 1`       | parity tests                           |
| `(low + high) // 2` | integer midpoint         | `0 & 9 → 4`       | binary search                          |

---
Key Insight

Both **Modulo (%)** and **Floor division (//)**:

* Help **keep values within a range**
* Avoid **out-of-bounds** or **overflow**
* Enable **efficient math manipulations** in algorithms
* Are constant time operations → **O(1)**
"""

# 3. Greatest Common Divisor (GCD) or Highest Common Factor (HCF)

# Idea
# Use the fact:    gcd(a, b) = gcd(b, a % b)
# Repeat until the remainder becomes 0; the last non-zero divisor is the GCD.

from math import gcd

gcd(a, b)

# Alternatively:
def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

# Use case -> Normalizing slopes in geometry

# LCM relation = lcm(a, b) = abs(a * b)/gcd(a, b) for non-zero a, b

print(gcd(252, 105)) # 21
print(gcd(1050,462)) # 42
print(gcd(108, 48)) # 12

# B. Modular Arithmetic (CRITICAL)

"""
Used whenever numbers overflow or wrap around.

Key Rules
(a + b) % m = (a % m + b % m) % m
(a * b) % m = (a % m * b % m) % m
"""

# Example 8 Fast Power (Binary Exponentiation)

def mod_pow(x, n, mod):
    res = 1
    while n:
        if n & 1:
            res = res * x % mod
        x = x * x % mod
        n >>= 1
    return res

"""
Used in:

-> Cryptography
-> Large exponent problems
-> Combinatorics
"""

# C. Bit Manipulation (Math Disguised as Bits)

"""
-----------------------------------------------------
Trick	            Meaning
-----------------------------------------------------
x & -x	            Lowest set bit
x ^ x = 0	        Duplicate cancellation
x & (x - 1)	        Remove lowest bit

Example 3: Single Number

result = 0
for num in nums:
    result ^= num
return result


Why it works:

-> XOR cancels identical numbers
-> Mathematical property: a ⊕ a = 0
"""

# D. Pigeonhole Principle

"""
If n + 1 objects go into n boxes, one box has ≥2 objects.

Example:

-> Duplicate number in array
-> Cycle detection
-> Hash collisions
"""

# Common Mistakes (Interview Killers)

"""
-> Using floating point slopes
-> Forgetting modulo during multiplication
"""

# 4. Sum of first N numbers (1 to N) -> S(n) = n * (n + 1) // 2

def sum_n(n: int) -> int:
    return n * (n + 1) // 2

# 5. Arithmetic Progression ->  a(n) = a(1) + (n - 1) * d

def ap_nth(a: int, d: int, n: int) -> int:
    return a + (n - 1) * d

# 6. Sum of Arithmetic Progression -> S(n) = (n // 2)*(2*a + (n - 1)*d)

def ap_sum(a: int, d: int, n: int) -> int:
    return (n * (2 * a + (n - 1) * d)) // 2

# 7. Geometric Progression -> a(n) = a * r ** (n - 1)

def gp_nth(a: int, r: int, n: int) -> int:
    return a * pow(r, n - 1)

# 8. Sum of Geometric Progression -> 
# S(n) = a * (r ** (n - 1) // (r - 1) for r != 1
# if r == 1, S(n) = n * a

def gp_sum(a: int, r: int, n: int) -> int:
    if r == 1:
        return n * a
    return a * (pow(r, n) - 1) // (r - 1)

# 9. Sum of Powers of Two -> S(n) = 2 ** (n + 1) - 1

def sum_powers_of_two(n: int) -> int:
    return (1 << (n + 1)) - 1

# 10. Permutation -> P(n, r) = n!//(n - r)!

from math import factorial

def permut(n: int, r: int) -> int:
    return factorial(n) // factorial(n - r)

# Alteratively

def _factorial(num: int) -> int:
    if num == 0:
        return 1
    return num * _factorial(num - 1)

def permutation(n: int, r: int) -> int:
    return _factorial(n) // _factorial(n - r)

# 11. Combination -> C(n, r) = n! // (r! * (n - r)!)

def combination(n: int, r: int):
    r = min(r, n - r)
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

