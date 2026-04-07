# Leetcode 2069. Walking Robot Simulation II

# https://leetcode.com/problems/walking-robot-simulation-ii/description/

# Tags -> Design, Simulation

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        # Total steps to complete one full loop
        self.perimeter = 2 * (width + height - 2)
        # 1D position tracking
        self.pos = 0
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        # Modulo arithmetic completely bypasses the simulation
        self.pos = (self.pos + num) % self.perimeter

    def get_pos(self) -> list[int]:
        p = self.pos
        
        # 1. Bottom edge (Moving East)
        if p < self.w:
            return [p, 0]
        # 2. Right edge (Moving North)
        elif p < self.w + self.h - 1:
            return [self.w - 1, p - (self.w - 1)]
        # 3. Top edge (Moving West)
        elif p < 2 * self.w + self.h - 2:
            # Start at right edge, subtract the steps moved along the top
            return [(self.w - 1) - (p - (self.w + self.h - 2)), self.h - 1]
        # 4. Left edge (Moving South)
        else:
            # Start at top edge, subtract the steps moved down the left side
            # Fun fact: mathematically this simplifies beautifully to self.perimeter - p
            return [0, self.perimeter - p]

    def get_dir(self) -> str:
        p = self.pos
        
        # The Edge Case: (0, 0)
        if p == 0:
            return "South" if self.moved else "East"
            
        if p < self.w:
            return "East"
        elif p < self.w + self.h - 1:
            return "North"
        elif p < 2 * self.w + self.h - 2:
            return "West"
        else:
            return "South"

# Complexity Analysis
"""
__init__: O(1)
step(num): O(1)
get_pos(): O(1)
get_dir(): O(1)

Space complexity: O(1)
"""
