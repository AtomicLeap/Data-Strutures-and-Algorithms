# Leetcode 421. Maximum XOR of Two Numbers in an Array

# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/

# 1. Bitwise Trie (prefix tree)

# Key idea: 
# For each number, to maximize XOR you try to pair each bit with 
# the opposite bit in the trie.
def find_max_xor(nums: list[int]) -> int:
    # Array-based trie for speed: children[bit] = next node index
    child0 = [-1]
    child1 = [-1]

    def new_node() -> int:
        child0.append(-1)
        child1.append(-1)
        return len(child0) - 1

    def insert(num: int) -> None:
        node = 0
        for b in range(30, -1, -1):
            bit = (num >> b) & 1
            if bit == 0:
                if child0[node] == -1:
                    child0[node] = new_node()
                node = child0[node]
            else:
                if child1[node] == -1:
                    child1[node] = new_node()
                node = child1[node]

    def query_best(num: int) -> int:
        node = 0
        best = 0
        for b in range(30, -1, -1):
            bit = (num >> b) & 1
            # Prefer opposite bit to make XOR bit = 1
            if bit == 0:
                if child1[node] != -1:
                    best |= (1 << b)
                    node = child1[node]
                else:
                    node = child0[node]
            else:
                if child0[node] != -1:
                    best |= (1 << b)
                    node = child0[node]
                else:
                    node = child1[node]
        return best

    insert(nums[0])
    result = 0
    for num in nums[1:]:
        result = max(result, query_best(num))
        insert(num)
    return result

# O(n * 31) - Time complexity
# O(n * 31) nodes worst-case - Space complexity 

# 2. Greedy Prefix-Set method

def find_max_xor_g(nums: list[int]) -> int:
    result = 0
    mask = 0

    for b in range(30, -1, -1):
        mask |= (1 << b)
        prefixes = {x & mask for x in nums}

        candidate = result | (1 << b)

        # Need: p ^ q = candidate  <=>  q = p ^ candidate
        possible = False
        for p in prefixes:
            if (p ^ candidate) in prefixes:
                possible = True
                break

        if possible:
            result = candidate

    return result

# O(n * 31) - Time complexity
# O(n) - Space complexity

print(find_max_xor([3,10,5,25,2,8])) # 28
print(find_max_xor([14,70,53,83,49,91,36,80,92,51,66,70])) # 127
print('---------------------------------------')
print(find_max_xor_g([3,10,5,25,2,8])) # 28
print(find_max_xor_g([14,70,53,83,49,91,36,80,92,51,66,70])) # 127
