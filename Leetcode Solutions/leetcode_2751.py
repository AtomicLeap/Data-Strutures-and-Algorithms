# Leetcode 2751. Robot Collisions

# https://leetcode.com/problems/robot-collisions/description

# Tags -> Array, Simulation, hard

def survived_robots(positions: list[int], healths: list[int], directions: str) -> list[int]:
    n = len(positions)
    robots = []
    stack = []

    for i in range(n):
        robots.append([i, positions[i], healths[i], directions[i]])

    robots.sort(key=lambda x: x[1])

    for i in range(n):
        idx, p, h, d = robots[i]

        if d == "R":
            stack.append([idx, p, h, d])
        else:
            while stack and stack[-1][3] == "R":
                if stack[-1][2] == h:
                    stack.pop()
                    h = 0
                    break
                elif stack[-1][2] > h:
                    stack[-1][2] -= 1
                    h = 0
                    break
                else:
                    stack.pop()
                    h -= 1

            if h:
                stack.append([idx, p, h, d])

    stack.sort(key=lambda x: x[0])

    results = []
    for idx, _, health, _ in stack:
        results.append(health)

    return results

# O(n log n) Time complexity due to sorting
# O(n) Space complexity for the robots list and stack

print(survived_robots([5,4,3,2,1], [2,17,9,15,10], "RRRRR")) # [2,17,9,15,10]
print(survived_robots([3,5,2,6], [10,10,15,12], "RLRL")) # [14]
print(survived_robots([1,2,5,6], [10,10,11,11], "RLRL")) # []




def survived_robots_i(positions: list[int], healths: list[int], directions: str) -> list[int]:
    n = len(positions)

    # Store: position, health, direction, original index
    robots = []
    for i in range(n):
        robots.append([positions[i], healths[i], directions[i], i])

    # Sort by position so collisions are processed spatially
    robots.sort(key=lambda x: x[0])

    stack = []  # indices in `robots` of alive right-moving robots

    for i in range(n):
        _, health, direction, original_idx = robots[i]

        if direction == 'R':
            stack.append(i)
        else:
            # Current robot moves left, may collide with previous right-movers
            while stack and robots[i][1] > 0:
                j = stack[-1]  # last unmatched right-moving robot

                if robots[j][1] < robots[i][1]:
                    # Right robot dies, left robot loses 1 health and continues
                    robots[i][1] -= 1
                    robots[j][1] = 0
                    stack.pop()
                elif robots[j][1] > robots[i][1]:
                    # Left robot dies, right robot loses 1 health
                    robots[j][1] -= 1
                    robots[i][1] = 0
                else:
                    # Equal health: both die
                    robots[j][1] = 0
                    robots[i][1] = 0
                    stack.pop()
                    break

    # Survivors in original input order
    survivors = []
    for _, health, _, original_idx in robots:
        if health > 0:
            survivors.append((original_idx, health))

    survivors.sort()  # restore original order
    return [health for _, health in survivors]

# O(n log n) Time complexity due to sorting
# O(n) Space complexity for the robots list and stack

print(survived_robots_i([5,4,3,2,1], [2,17,9,15,10], "RRRRR")) # [2,17,9,15,10]
print(survived_robots_i([3,5,2,6], [10,10,15,12], "RLRL")) # [14]
print(survived_robots_i([1,2,5,6], [10,10,11,11], "RLRL")) # []]