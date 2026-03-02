# Leetcode 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/description/

# Tags -> String, Greedy

def min_partitions(n: str) -> int:
        # The answer is the maximum digit in n
        max_digit = 0
        for char in n:
            digit = ord(char) - ord('0')
            if digit > max_digit:
                max_digit = digit
        return max_digit

# O(|n|) - Time complexity
# O(1) - Space complexity

print(min_partitions("32")) # 3
print(min_partitions("82734")) # 8
print(min_partitions("27346209830709182346")) # 9
