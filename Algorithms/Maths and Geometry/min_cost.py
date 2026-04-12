# 3789. Minimum Cost to Acquire Required Items

# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/description/

# Tags -> Math, Greedy


def minimum_cost(
    cost1: int,
    cost2: int,
    cost_both: int,
    need1: int,
    need2: int
) -> int:
    def total_cost(x: int) -> int:
        return (
            x * cost_both
            + max(0, need1 - x) * cost1
            + max(0, need2 - x) * cost2
        )

    a = min(need1, need2)
    b = max(need1, need2)

    return min(
        total_cost(0),
        total_cost(a),
        total_cost(b),
    )
    
# O(1) Time complexity - We only check a constant number of scenarios (0, min(need1, need2), max(need1, need2))
# O(1) Space complexity - We use only a constant amount of extra space

print(minimum_cost(1, 2, 3, 1, 2)) # 5
print(minimum_cost(2, 3, 4, 1, 1)) # 4
print(minimum_cost(1, 1, 1, 2, 2)) # 4

