# Leetcode 875. Koko Eating Bananas

def min_eating_speed(piles: list[int], h: int) -> int:
    left, right = 1, max(piles)

    def hours_needed(k: int) -> int:
        # sum of ceil(p/k) without floats: (p + k - 1) // k
        total = 0
        for p in piles:
            total += (p + k - 1) // k
        return total

    while left < right:
        mid = (left + right) // 2
        if hours_needed(mid) <= h:
            right = mid  # mid works, try smaller
        else:
            left = mid + 1  # mid too slow
    return left

print(min_eating_speed([3,6,7,11], 8)) # 4
print(min_eating_speed([30,11,23,4,20], 5)) # 30
print(min_eating_speed([30,11,23,4,20], 6)) # 23
