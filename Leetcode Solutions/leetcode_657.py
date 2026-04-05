# Leetcode 657. Robot Return to Origin

# https://leetcode.com/problems/robot-return-to-origin/description

# Tags -> String, Simulation
def judge_circle(moves: str) -> bool:
    return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

# O(n) - Time complexity
# O(1) - Space complexity

print(judge_circle("UD"))  # Output: true
print(judge_circle("LL"))  # Output: false
print(judge_circle("URDL"))  # Output: true
print(judge_circle("LDRRLRUULR"))  # Output: false

def judge_circle_i(moves: str) -> bool:
    x, y = 0, 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1

    return x == 0 and y == 0

# O(n) - Time complexity
# O(1) - Space complexity

print(judge_circle_i("UD"))  # Output: true
print(judge_circle_i("LL"))  # Output: false
print(judge_circle_i("URDL"))  # Output: true
print(judge_circle_i("LDRRLRUULR"))  # Output: false