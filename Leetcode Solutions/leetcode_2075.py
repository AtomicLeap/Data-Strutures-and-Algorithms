# Leetcode 2075. Decode the Slanted Ciphertext

# https://leetcode.com/problems/decode-the-slanted-ciphertext/description

# Tags -> String, Simulation


def decode_ciphertext(encoded_text: str, rows: int) -> str:
    if rows == 0 or not encoded_text:
        return ""
    
    cols = len(encoded_text) // rows
    result = []

    for start_col in range(cols):
        r, c = 0, start_col
        while r < rows and c < cols:
            result.append(encoded_text[r * cols + c])
            r += 1
            c += 1

    return "".join(result).rstrip()
    
# O(n) - Time complexity
# O(n) - Space complexity

print(decode_ciphertext("ch   ie   pr", 3))  # Output: "cipher"
print(decode_ciphertext("iveo    eed   l te   olc", 4))  # Output: "i love leetcode"
print(decode_ciphertext("coding", 1))  # Output: "coding"


def decode_ciphertext_i(encoded_text: str, rows: int) -> str:
    if rows == 1:
        return encoded_text

    N = len(encoded_text)
    cols = N // rows
    i, j, k = 0, 0, 0
    original_text = []

    while k < N:
        original_text.append(encoded_text[k])
        i += 1
        if i == rows:
            i = 0
            j += 1
        k = i*(cols + 1) + j

    return ''.join(original_text).rstrip()
    
# O(n) - Time complexity
# O(n) - Space complexity

print(decode_ciphertext_i("ch   ie   pr", 3))  # Output: "cipher"
print(decode_ciphertext_i("iveo    eed   l te   olc", 4))  # Output: "i love leetcode"
print(decode_ciphertext_i("coding", 1))  # Output: "coding"

