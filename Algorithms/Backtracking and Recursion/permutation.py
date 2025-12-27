# Permutation of Numbers

# Using Backtracking technique
# Backtracking = DFS + undo + pruning
def permutation(nums: list[int]):
    n = len(nums)
    results = []

    def backtrack(combination: list[int], table: list[bool]):
        # Base case
        if len(combination) == n:
            results.append(combination[:])
            return

        for i in range(n):
            if table[i]: # PRUNING
                continue

            table[i] = True
            combination.append(nums[i])

            backtrack(combination, table)

            combination.pop() # UNDO
            table[i] = False # UNDO

    backtrack([], [False] * n)
    return results

print(permutation([3, 4, 5]))
print(permutation([1, 2, 3, 4]))