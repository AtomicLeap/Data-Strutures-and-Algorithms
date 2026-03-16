# Leetcode 1622. Fancy Sequence

# https://leetcode.com/problems/fancy-sequence/description/

# Tags -> Design

# Idea
"""
number = (base * mul + sum) % MOD

n = (b . m + s) % MOD
b = (n - s).(m ^ -1) % MOD
b = ((n - s).pow(m, -1, MOD) % MOD)

When we have AddAll (inc):
n = (b . m + s) + inc = b . m + (s + inc)

When we have MultAll (ms):
n = (b . m + s) * ms = b . (m . ms) + (s + ms)
"""

class FancySequence:
    MOD = 10**9 + 7

    def __init__(self):
        self.results = []
        self.mul = 1
        self.add = 0
        
    def append(self, val: int) -> None:
        base = ((val - self.add) * pow(self.mul, -1, self.MOD)) % self.MOD
        self.results.append(base)
        
    def add_all(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def mult_all(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD
        
    def get_index(self, idx: int) -> int:
        if idx >= len(self.results):
            return -1
        return self.results[idx] * self.mul + self.add

# O(1) - Time complexity
# O(n) - Space complexity