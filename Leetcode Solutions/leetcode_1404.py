# Leetcode 1404. Number of Steps to Reduce a Number in Binary Representation to One

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

# Tags -> String, Bit manipulation

def num_of_steps(s: str) -> int:
    steps = 0
    carry = 0
    
    # Traverse from right to left (excluding MSB - The Most Significant Bit)
    for i in range(len(s) - 1, 0, -1):
        bit = int(s[i])
        effective_bit = bit + carry
        
        if effective_bit == 0:
            # even → divide by 2
            steps += 1
        elif effective_bit == 1:
            # odd → add 1 (carry) then divide
            steps += 2
            carry = 1
        else:  # effective_bit == 2
            # even (10 in binary)
            steps += 1
            carry = 1
    
    # If carry remains at MSB
    if carry == 1:
        steps += 1
    
    return steps

# O(n) - Time complexity
# O(1) - Space complexity

print(num_of_steps("1101")) # 6
print(num_of_steps("10")) # 1
print(num_of_steps("1")) # 0
