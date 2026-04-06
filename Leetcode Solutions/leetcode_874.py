# Leetcode 874. Walking Robot Simulation

# https://leetcode.com/problems/walking-robot-simulation/description

# Tags -> String, Simulation

# Idea
"""
Use direct simulation with an obstacle hash set.
Because each forward command is at most 9, we can safely move the robot 
one step at a time. At each step:

-> compute the next cell
-> if it is an obstacle, stop this command
-> otherwise move there
-> update the maximum squared distance

This is efficient enough since:
-> commands.length <= 10^4
-> each move command is at most 9

So the total number of unit steps is at most 9 * 10^4, which is fine.
Track:

-> current position (x, y)
-> current direction
-> best answer max_dist

Represent directions as:
-> north = (0, 1)
-> east = (1, 0)
-> south = (0, -1)
-> west = (-1, 0)

Then:

-2 means turn left
-1 means turn right
positive k means try to move k times, one unit each time

Store all obstacles in a set of tuples for O(1) average lookup.
"""

def robot_sim(commands: list[int], obstacles: list[list[int]]) -> int:
    obstacle_set = {tuple(ob) for ob in obstacles}

    # North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0  # start facing north

    x = 0
    y = 0
    max_dist = 0

    for cmd in commands:
        if cmd == -2:          # turn left
            d = (d - 1) % 4
        elif cmd == -1:        # turn right
            d = (d + 1) % 4
        else:                  # move forward cmd steps
            dx, dy = directions[d]
            for _ in range(cmd):
                nx = x + dx
                ny = y + dy

                if (nx, ny) in obstacle_set:
                    break

                x, y = nx, ny
                max_dist = max(max_dist, x * x + y * y)

    return max_dist

# Complexity Analysis
"""
Let:

n = len(commands)
m = len(obstacles)

Then:

building obstacle set: O(m)
simulation: at most 9n unit moves, so O(n)

Overall:

Time: O(m + n)
Space: O(m)
"""

print(robot_sim([4, -1, 3], []))  # Output: 25
print(robot_sim([4, -1, 4, -2, 4], [[2, 4]]))  # Output: 65
