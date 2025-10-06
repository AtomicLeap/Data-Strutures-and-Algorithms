# Maths Operators Recipe

# 1. modulo (%) operator
# 2. floor division (//) operator
# 3. greatest common divisor (gcd)

"""
# Modulo operator (%)

Returns the **remainder** after dividing one number by another.
a % b = remainder when a is divided by b

Example:
7 % 3  # = 1  (since 3*2 = 6, remainder = 1)

Key property:
a = (a // b) * b + (a % b)

# Floor division (//)

Divides two numbers and **rounds down** to the nearest integer (toward negative infinity).
a // b = floor(a / b)

Example:
7 // 3  # = 2

Another example (with negatives):
-7 // 3  # = -3  (since floor(-2.333) = -3)
-7 % 3   # = 2   (since -7 = (-3)*3 + 2)

USES
Both `%` and `//` are used in:

1. Array indexing
2. Hashing
3. Digit extraction
4. Cycle detection
5. Circular buffers / queues
6. Number manipulation problems
7. Mathematical patterns (LCM, GCD, modular arithmetic)

Practical Uses and Examples
Example 1: Extracting digits (used in math-based problems)

Suppose you need to **reverse digits** of an integer `x = 1234`.

```python
rev = 0
x = 1234
while x > 0:
    digit = x % 10       # get last digit
    rev = rev * 10 + digit
    x //= 10             # remove last digit
print(rev)  # Output: 4321
```
Why it works:
1. `% 10` isolates the last digit.
2. `// 10` removes the last digit.

Used in problems like:
* Reversing integers
* Palindrome numbers
* Counting digits
---

Example 2: Circular array / rotation

In a **circular array**, indices wrap around.
For example, moving 1 step forward from index `n-1` should go back to `0`.

```python
arr = [10, 20, 30, 40]
n = len(arr)
index = (3 + 1) % n   # move one step forward from last element
print(index)  # 0
```

Why it works:
Modulo keeps index within bounds of `[0, n-1]`.

Used in:
* Rotating arrays
* Circular queues
* Hash tables (open addressing)
---

Example 3: Hash function in Hash Tables

```python
key = 12345
table_size = 10
index = key % table_size
```

Why it works:**
Modulo distributes keys evenly across slots `0..9`.

Used in:
* Hash maps
* Bloom filters
* Cuckoo hashing

---

Example 4: Even/Odd checking

```python
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

*Why it works:**
Modulo quickly checks divisibility.

Used in:
* Bitmask problems
* Parity checks
* Alternating sequences

---

Example 5: Working with time or cycles

**Problem:** What time will it be 9 hours after 11 o’clock?

```python
time = (11 + 9) % 12
print(time)  # 8
```

Why it works:
The modulo "wraps around" the 12-hour clock.
---

Example 6: Finding middle index (using floor division)

Used in **binary search** or **merge sort**.

```python
low, high = 0, n - 1
mid = (low + high) // 2
```

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

```python
colors = ["red", "green", "blue"]
for i in range(10):
    print(colors[i % 3])
```

Output cycles: red → green → blue → red → …
---

Example 8: Modular arithmetic (in big number problems)
Used in problems like:

* Large Fibonacci numbers
* Modular exponentiation
* Cryptography (RSA, etc.)

```python
MOD = 1_000_000_007
result = (a + b) % MOD
```

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

# greatest common divisor (GCD) or Highest Common Factor (HCF)

# Idea
# Use the fact:    gcd(a, b) = gcd(b, a % b)
# Repeat until the remainder becomes 0; the last non-zero divisor is the GCD.

def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


# LCM relation = lcm(a, b) = abs(a * b)/gcd(a, b) for non-zero a, b

print(gcd(252, 105)) # 21
print(gcd(1050,462)) # 42
print(gcd(108, 48)) # 12
