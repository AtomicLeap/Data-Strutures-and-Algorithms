# Leetcode 401. Binary Watch

# https://leetcode.com/problems/binary-watch/description

"""
We just need to try all valid times on the watch and keep the ones whose total number of 1-bits in (hour, minute) equals turnedOn.
1. Hours range: 0..11 (4 LEDs)
2. Minutes range: 0..59 (6 LEDs)
3. Total possibilities: 12 * 60 = 720 → tiny, so brute force is optimal and simplest.
"""

# Key idea
"""
For a time h:m, the number of LEDs ON is:
    popcount(h) + popcount(m)
If it equals turnedOn, include it.
Minutes must be formatted with 2 digits: f"{m:02d}".
"""
def read_binary_watch(turned_on: int) -> list[str]:
    result = []
    for h in range(12):
        hb = h.bit_count()
        for m in range(60):
            if hb + m.bit_count() == turned_on:
                result.append(f"{h}:{m:02d}")
    return result

# 12 * 60 = 720 checks → O(1) - Time complexity
# O(n) - Space complexity

print(read_binary_watch(1)) # ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
print(read_binary_watch(9)) # []
