# Leetcode 3013. Divide an Array Into Subarrays With Minimum Cost II

# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description

from heapq import heappush, heappop
from collections import defaultdict

def minimum_cost(nums: list[int], k: int, dist: int) -> int:
    n = len(nums)
    m = k - 2                     # how many starts besides i1 and 0
    last_s = n - k + 1            # i1 can be at most n-k+1

    # heaps store (value, idx) or (-value, idx)
    small = []  # max-heap via (-val, idx): holds m smallest elements
    large = []  # min-heap via (val, idx): holds the rest

    delayed_small = defaultdict(int)
    delayed_large = defaultdict(int)

    in_small = {}                 # idx -> bool
    small_sz = 0                  # live elements in small
    large_sz = 0                  # live elements in large
    sum_small = 0                 # sum of live elements in small

    def prune_small():
        while small:
            negv, idx = small[0]
            if delayed_small[idx]:
                heappop(small)
                delayed_small[idx] -= 1
                if delayed_small[idx] == 0:
                    del delayed_small[idx]
            else:
                break

    def prune_large():
        while large:
            v, idx = large[0]
            if delayed_large[idx]:
                heappop(large)
                delayed_large[idx] -= 1
                if delayed_large[idx] == 0:
                    del delayed_large[idx]
            else:
                break

    def move_small_to_large():
        nonlocal small_sz, large_sz, sum_small
        prune_small()
        negv, idx = heappop(small)
        v = -negv
        sum_small -= v
        small_sz -= 1
        heappush(large, (v, idx))
        large_sz += 1
        in_small[idx] = False

    def move_large_to_small():
        nonlocal small_sz, large_sz, sum_small
        prune_large()
        v, idx = heappop(large)
        large_sz -= 1
        heappush(small, (-v, idx))
        small_sz += 1
        sum_small += v
        in_small[idx] = True

    def rebalance():
        # ensure small_sz == m (as long as possible)
        prune_small()
        prune_large()
        while small_sz > m:
            move_small_to_large()
            prune_small()
        while small_sz < m and large_sz > 0:
            move_large_to_small()
            prune_large()
        prune_small()
        prune_large()

    def add(idx: int):
        nonlocal small_sz, large_sz, sum_small
        v = nums[idx]

        prune_small()
        if small_sz < m:
            heappush(small, (-v, idx))
            small_sz += 1
            sum_small += v
            in_small[idx] = True
        else:
            # compare to largest among the m-smallest (top of max-heap)
            largest_small = -small[0][0] if small else float("inf")
            if v <= largest_small:
                heappush(small, (-v, idx))
                small_sz += 1
                sum_small += v
                in_small[idx] = True
            else:
                heappush(large, (v, idx))
                large_sz += 1
                in_small[idx] = False

        rebalance()

    def remove(idx: int):
        nonlocal small_sz, large_sz, sum_small
        v = nums[idx]
        if in_small.get(idx, False):
            delayed_small[idx] += 1
            sum_small -= v
            small_sz -= 1
        else:
            delayed_large[idx] += 1
            large_sz -= 1
        in_small.pop(idx, None)
        rebalance()

    # Initialize window for s = 1:
    # window indices are [s+1 .. min(n-1, s+dist)] = [2 .. min(n-1, 1+dist)]
    end = min(n - 1, 1 + dist)
    for idx in range(2, end + 1):
        add(idx)

    results = float("inf")

    for s in range(1, last_s + 1):
        # current window is [s+1 .. min(n-1, s+dist)]
        # must have at least m elements; guaranteed by constraints and s range
        results = min(results, nums[0] + nums[s] + sum_small)

        # slide s -> s+1
        out_idx = s + 1
        old_end = min(n - 1, s + dist)
        if out_idx <= old_end:
            remove(out_idx)

        in_idx = s + dist + 1
        if in_idx <= n - 1:
            add(in_idx)

    return results

# O(n log dist) - Time complexity
# O(dist) - Space complexity


print(minimum_cost([1,3,2,6,4,2], 3, 3)) # 5
print(minimum_cost([10,1,2,2,2,1], 4, 3)) # 15
print(minimum_cost([10,8,18,9], 3, 1)) # 36
