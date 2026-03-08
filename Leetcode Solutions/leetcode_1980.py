# Leetcode 1980. Find Unique Binary String

# https://leetcode.com/problems/find-unique-binary-string/description/

# Tags -> String, Array

# Use Cantor's diagonalization
def find_different_binary_string(nums: list[str]) -> str:
    unique_string = ""

    for idx in range(len(nums)):
        if nums[idx][idx] == "0":
            unique_string += "1"
        else:
            unique_string += "0"
    return unique_string

print(find_different_binary_string(["01","10"])) # "11"
print(find_different_binary_string(["00","01"])) # "11"
print(find_different_binary_string(["111","011","001"])) # "101"
