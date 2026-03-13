# Leetcode 3296. Minimum Number of Seconds to Make Mountain Height Zero

# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/description/

# Tags -> Maths, Binary Search

from math import isqrt

def min_number_of_seconds(mountain_height: int, worker_times: list[int]) -> int:
    def can_finish(time_limit: int) -> bool:
        total_reduced = 0

        for w in worker_times:
            # Solve: w * x * (x + 1) / 2 <= time_limit
            # => x(x + 1) <= 2 * time_limit // w
            k = (2 * time_limit) // w
            x = (isqrt(1 + 4 * k) - 1) // 2
            total_reduced += x

            if total_reduced >= mountain_height:
                return True

        return False

    low = 0
    high = min(worker_times) * mountain_height * (mountain_height + 1) // 2

    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid
        else:
            low = mid + 1

    return low

print(min_number_of_seconds(4, [2, 1, 1])) # 3
print(min_number_of_seconds(10, [3,2,2,4])) # 12
print(min_number_of_seconds(5, [1])) # 15
