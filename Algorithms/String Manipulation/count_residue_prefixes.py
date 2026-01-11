# Leetcode 3803. Count Residue Prefixes

# https://leetcode.com/problems/count-residue-prefixes/description/

def count_residue_prefixes(s: str) -> int:
    count = 0
    visited = set()
    for i in range(len(s)):
        visited.add(s[i])
        if (i + 1) % 3 == len(visited):
            count += 1
        else:
            continue
    return count

# n = len(s)
# O(n) - Time complexity
# O(n) - Space complexity


print(count_residue_prefixes("abc")) # 2
print(count_residue_prefixes("dd")) # 1
print(count_residue_prefixes("bob")) # 2
print(count_residue_prefixes("bbbb")) # 2