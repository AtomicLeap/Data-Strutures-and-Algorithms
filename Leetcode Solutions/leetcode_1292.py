# Leetcode 1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold

# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description

# Key idea
"""
Use a 2D prefix-sum so you can query any square sum in O(1), then 
binary search the side length k (since if a k x k square fits, any smaller 
size can also fit).

Build ps where ps[i][j] = sum of submatrix mat[0..i-1][0..j-1].

Square sum with top-left (r, c) and size k:
    sum(r, c, k) = ps[r+k][c+k] - ps[r][c+k] - ps[r+k][c] + ps[r][c]
Then for a fixed k, check all positions (r,c) in O(mn); each check is O(1).

Why binary search is valid?
If there exists a square of side k with sum ≤ threshold, then some square 
of any smaller side k-1, k-2, ... also exists (you can take a smaller 
square inside it; with nonnegative values the sum can only decrease). 
So feasibility is monotonic.
"""

def max_side_length(mat: list[list[int]], threshold: int) -> int:
    m, n = len(mat), len(mat[0])

    # 2D prefix sum: ps has size (m+1) x (n+1)
    ps = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        row_sum = 0
        for j in range(n):
            row_sum += mat[i][j]
            ps[i + 1][j + 1] = ps[i][j + 1] + row_sum

    def square_sum(r: int, c: int, k: int) -> int:
        r2, c2 = r + k, c + k
        return ps[r2][c2] - ps[r][c2] - ps[r2][c] + ps[r][c]

    def exists(k: int) -> bool:
        if k == 0:
            return True
        for r in range(0, m - k + 1):
            for c in range(0, n - k + 1):
                if square_sum(r, c, k) <= threshold:
                    return True
        return False

    lo, hi = 0, min(m, n)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if exists(mid):
            lo = mid
        else:
            hi = mid - 1
    return lo


# Complexities
"""
Prefix sum: O(mn)
Binary search over k up to min(m,n) (≤ 300): O(log(min(m,n)))
Each feasibility check: O(mn)
Total Time complexity: O(mn log(min(m,n))), fits easily for 300 x 300.

Space Complexity: O(m · n)
"""

print(max_side_length([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)) # 2
print(max_side_length([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1)) # 0
