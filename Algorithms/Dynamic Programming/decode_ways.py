# Leetcode 91. Decode Ways

# https://leetcode.com/problems/decode-ways/description/

def num_decodings(s: str) -> int:
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

    two = 1        
    one = 1        

    for i in range(1, n):
        curr = 0

        # Single-digit decode (s[i])
        if s[i] != '0':
            curr += one

        # Two-digit decode (s[i-1:i+1])
        pair = int(s[i-1:i+1])
        if 10 <= pair <= 26:
            curr += two

        if curr == 0:     # no valid decoding at this step
            return 0

        two, one = one, curr

    return one

# O(n) Time complexity
# O(1) Space complexity

print(num_decodings("12")) # 2
print(num_decodings("226")) # 3
print(num_decodings("06")) # 0