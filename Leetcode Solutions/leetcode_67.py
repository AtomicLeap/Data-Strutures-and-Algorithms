# Leetcode 67. Add Binary

# https://leetcode.com/problems/add-binary/description/

def add_binary(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        total = carry

        if i >= 0:
            total += int(a[i])
            i -= 1

        if j >= 0:
            total += int(b[j])
            j -= 1

        result.append(str(total % 2))
        carry = total // 2

    return ''.join(reversed(result))

# O(n) - Time complexity
# O(n) - Space complexity

print(add_binary('11', '1')) # 1
print(add_binary("1010", "1011")) # "10101"


def add_binary_z(a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = []

        for i in range(max_len - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append('1')

        return ''.join(reversed(result))

# O(n) - Time complexity
# O(n) - Space complexity

print(add_binary_z('11', '1')) # 1
print(add_binary_z("1010", "1011")) # "10101"
