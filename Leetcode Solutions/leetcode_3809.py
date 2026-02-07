# Leetcode 3809. Best Reachable Tower

# https://leetcode.com/problems/best-reachable-tower/description/

def best_reachable_tower(towers: list[int, int, int], center: list[int, int], radius: int) -> [int, int, int]:
    reachable_towers = []

    for tower in towers:
        distance = abs(tower[0] - center[0]) + abs(tower[1] - center[1])
        if (distance <= radius):
            reachable_towers.append(tower)
    sorted_reachable_towers = sorted(reachable_towers, key=lambda x: (-x[2], x[0], x[1]))
    return sorted_reachable_towers[0][:2] if sorted_reachable_towers else [-1, -1]

# O (n * log n) - Time complexity
# O (n) - Space compexity

print(best_reachable_tower([[1, 2, 5], [2, 1, 7], [3, 1, 9]], [1, 1], 2)) # [3, 1]
print(best_reachable_tower([[1, 3, 4], [2, 2, 4], [4, 4, 7]], [0, 0], 5)) # [1, 3]

