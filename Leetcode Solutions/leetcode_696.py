# Leetcode 696. Count Binary Substrings

# https://leetcode.com/problems/count-binary-substrings/description/

def count_binary_substrings(s: str) -> int:
    prev = 0          # length of previous run
    curr = 1          # length of current run (at least 1)
    result = 0

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            curr += 1
        else:
            result += min(prev, curr)
            prev = curr
            curr = 1

    result += min(prev, curr)  # last boundary contribution
    return result

# O(n) - Time complexity
# O(1) - Space complexity

print(count_binary_substrings("00110011")) # 6
print(count_binary_substrings("10101")) # 4
