# Leetcode 1888. Minimum Number of Flips to Make the Binary String Alternating

# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/

# Tags -> String, Not Manipulation

def min_flips(s: str) -> int:
    s = s + s
    n = len(s) // 2

    count1 = 0   # mismatches with pattern 1010...
    count2 = 0   # mismatches with pattern 0101...
    left = 0
    num_of_flips = float("inf")

    for right in range(len(s)):
        if right % 2 == 0:
            str_type_1 = '1'
            str_type_2 = '0'
        else:
            str_type_1 = '0'
            str_type_2 = '1'

        if s[right] != str_type_1:
            count1 += 1
        if s[right] != str_type_2:
            count2 += 1

        # Keep window size equal to original string length
        if right - left + 1 > n:
            if left % 2 == 0:
                left_type_1 = '1'
                left_type_2 = '0'
            else:
                left_type_1 = '0'
                left_type_2 = '1'

            if s[left] != left_type_1:
                count1 -= 1
            if s[left] != left_type_2:
                count2 -= 1

            left += 1

        # Check each rotation window
        if right - left + 1 == n:
            num_of_flips = min(num_of_flips, count1, count2)

    return num_of_flips

# O(n) - Time complexity
# O(1) - Space complexity

print(min_flips("111000")) # 2
print(min_flips("010")) # 0
print(min_flips("1110")) # 1
print(min_flips("111000")) # 2
