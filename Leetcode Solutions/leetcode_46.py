# Leetcode 46. Permutations

# https://leetcode.com/problems/permutations/description/

# Tags -> Backtracking

def permute(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    results = []
    combination = []
    visited = [False] * n

    def backtrack():
        if len(combination) == n:
            results.append(combination.copy())
            return
        
        for idx in range(n):
            if visited[idx]:
                continue
    
            visited[idx] = True
            combination.append(nums[idx])

            backtrack()

            combination.pop()
            visited[idx] = False

    backtrack()
    return results

# O(n > n!) - Time complexity
# O(n > n!) - Space complexity


print(permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
print(permute([0, 1])) # [[0, 1],[1, 0]]
print(permute([1])) # [[1]]