# Leetcode 6. Zigzag Conversion

# https://leetcode.com/problems/zigzag-conversion/description/

# Tags -> String

def convert(s: str, num_rows: int) -> str:
    if num_rows >= len(s) or num_rows == 1:
        return s
    results = [""] * num_rows
    is_going_down = False
    row = 0
    
    for char in s:
        results[row] += char

        if row == 0 or row == num_rows - 1:
            is_going_down = not is_going_down
        
        row += 1 if is_going_down else -1
    return ''.join(results)

# Let m, n = number of rows, len(s)
# O(n) - Time complexity
# O(m) - Space complexity -> Worst case -> O(n)

print(convert("PAYPALISHIRING", 3)) # "PAHNAPLSIIGYIR"
print(convert("PAYPALISHIRING", 4)) # "PINALSIGYAHRPI"
print(convert("A", 1)) # "A"