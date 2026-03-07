# Leetcode 1758. Minimum Changes To Make Alternating Binary String

# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

# Tags -> String

def min_operations(s: str) -> int:
    count1 = 0
    count2 = 0

    for i in range(len(s)):
        if i % 2 == 0:
            str_type_1 = '1'
        else:
            str_type_1 = '0'
        if s[i] != str_type_1:
            count1 += 1
        else:
            count2 += 1
    return min(count1, count2)

# O(n) - Time complexity
# O(1) - Space complexity

print(min_operations("111000")) # 2
print(min_operations("010")) # 0
print(min_operations("1110")) # 1
print(min_operations("111000")) # 2