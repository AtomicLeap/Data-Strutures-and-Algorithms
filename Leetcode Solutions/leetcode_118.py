# Leetcode 118. Pascal's Triangle

# https://leetcode.com/problems/pascals-triangle/description/

# Tags -> Array, Dynamic Programming

def generate(num_rows: int) -> list[list[int]]:
    table = []

    for r in range(num_rows):
        row = [1] * (r + 1)
        for c in range(1, r):
            row[c] = table[r - 1][c - 1] + table[r - 1][c]
        table.append(row)

    return table

# O(num_rows^2) Time complexity, where num_rows is the input number
# O(num_rows^2) Space complexity, where num_rows is the input number

print(generate(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(generate(1)) # [[1]]      
print(generate(2)) # [[1], [1, 1]]


# Alternative (Combinatorics / Binomial Coefficient — Faster per row)
"""
Using:
C(n, k) = n! / (k! * (n - k)!)
      
We can compute each row in O(n).
"""
def generate_c(num_rows: int) -> list[list[int]]:
    table = []

    for n in range(num_rows):
        row = [1]
        for k in range(1, n + 1):
            row.append(row[-1] * (n - k + 1) // k)
        table.append(row)

    return table

# O(num_rows^2) Time complexity, where num_rows is the input number
# O(num_rows^2) Space complexity, where num_rows is the input number

print(generate_c(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print(generate_c(1)) # [[1]]
print(generate_c(2)) # [[1], [1, 1]]
