# Leetcode 77. Combinations

# https://leetcode.com/problems/combinations/description/

# Tags -> Backtracking

def combine(n: int, k: int) -> list[list[int]]:
    results = []
    combination = []

    def backtrack(start: int):
        if len(combination) == k:
            results.append(combination[:])
            return
        
        # Pruning optimization
        remaining = k - len(combination)

        for idx in range(start, n - remaining + 2):
            combination.append(idx)
            backtrack(idx + 1)
            combination.pop()

    backtrack(1)
    return results

# Let C(n, k) = n! / (k!(n-k)!)
# O(C(n,k) * k) - Time complexity
# O(k) Recursive depth + O(n) for output results - Space complexity

print(combine(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(combine(1, 1)) # [[1]]


# Alternative simple solution without Pruning
def combine_a(n: int, k: int):
    results = []

    def dfs(start, combination):
        if len(combination) == k:
            results.append(combination[:])
            return

        for i in range(start, n + 1):
            dfs(i + 1, combination + [i])

    dfs(1, [])
    return results

# Let C(n, k) = n! / (k!(n-k)!)
# O(C(n,k) * k) - Time complexity
# O(k) Recursive depth + O(n) for output results - Space complexity

print(combine_a(4, 2)) # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(combine_a(1, 1)) # [[1]]
