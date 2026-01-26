# Leetcode 2975. Maximum Square Area by Removing Fences From a Field

# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/

#Key Idea
"""
A square sub-field is defined by choosing two horizontal fences (its top/bottom) 
and two vertical fences (its left/right).
If the vertical distance between the chosen horizontal fences equals the 
horizontal distance between the chosen vertical fences, we can form a square of 
side L.

So we need the largest L such that:
1. L is a distance between two horizontal fence lines, and
2. L is also a distance between two vertical fence lines.

The outer borders (1 and m) and (1 and n) are fences too (and cannot be removed), 
so include them.
"""

# Efficient approach (k ≤ 602)
"""
1. Build arrays:
    - H = sorted(hFences + [1, m])
    - V = sorted(vFences + [1, n])
2. Compute all pairwise distances in H → set Hd
3. Compute all pairwise distances in V → set Vd
4. Find the maximum value in Hd ∩ Vd. If none, return -1.
5. Answer = L^2 mod (1e9+7).

Time is O(|H|^2 + |V|^2) which is fine for up to ~602.
"""

MOD = 10**9 + 7

def maximize_square_area(m: int, n: int, h_fences: list[int], v_fences: list[int]) -> int:
    H = sorted(h_fences + [1, m])
    V = sorted(v_fences + [1, n])

    def all_diffs(arr: list[int]) -> set[int]:
        diffs = set()
        L = len(arr)
        for i in range(L):
            ai = arr[i]
            for j in range(i + 1, L):
                diffs.add(arr[j] - ai)
        return diffs

    h_d = all_diffs(H)
    v_d = all_diffs(V)

    # Intersect smartly by iterating the smaller set
    if len(h_d) > len(v_d):
        h_d, v_d = v_d, h_d

    best = 0
    for d in h_d:
        if d in v_d and d > best:
            best = d

    if best == 0:
        return -1
    return (best * best) % MOD

# Let k = len(hFences) + 2 ≤ 602, l = len(vFences) + 2 ≤ 602
# Time complexity: O(k^2 + l^2) (≈ at most ~2 * 600² = 720k operations)
# Space complexity: O(k^2 + l^2) for the distance sets

print(maximize_square_area(4, 3, [2,3], [2])) # 4
print(maximize_square_area(6, 7, [2], [4])) # -1