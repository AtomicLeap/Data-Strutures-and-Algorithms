# Common Algorithms

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Kadane Algorithm
"""
Maximum Subarray
"""

# 2. Dutch National Flag algorithm [three-pointer]
"""
Sort Colors
"""

# 3. Prefix Sum + HashMap
"""
Subarray Sum Equals K
"""

# 4. Floyd’s Cycle Detection Algorithm (also called the Tortoise and Hare algorithm)
# 2-Pointer (Slow and Fast) Algorithm.

# 4a. For Linked List - Detect a cycle
def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next          
        fast = fast.next.next     
        
        if slow == fast:          # pointers meet → cycle detected
            return True
    
    return False

# 4b. For Array (List) - Find duplicate
def find_duplicate(nums: list[int]) -> int:
    # Phase 1: find intersection point in the cycle
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: find entrance to the cycle (duplicate)
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# 5. Palindrone Problem - Alternative Solution with O(n) Space
# Method -> List Element Equality

def is_palindrome(head):
    if not head or not head.next:
        return True

    results = []

    while head:
        results.append(head.val)
        head = head.next
    return results == results[::-1]

# 6. Brian Kernighan’s Algorithm - For Counting set bits
# Clear lowest set bit ->
"""
n = n & (n - 1) -> remove a set bit
"""
def count_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

# 6a.check odd number
# If a number has its lowest bit = 1, it’s odd.
# Instead of % 2, you can check:
"""
if n & 1:  # faster than n % 2
    print("Odd")
"""

# 6b. Power of Two
# An integer n is a power of two, if there exists an integer 
# x such that n == 2^x.
def is_power_of_two(n: int) -> bool:
    return n > 0 and n & (n - 1) == 0

# 6c. Check if two numbers have opposite signs
"""
if (a ^ b) < 0:
    print("Opposite signs")
"""

# 6d. Check a numbers Lowest set bit

"""
Given number: n

lowest_bit = n & -n
"""

# 7. XOR

# 7a. XOR for Finding Unique Numbers
# In an array where every number appears twice except one, 
# XOR finds the odd one out in O(n):
"""
nums = [2, 3, 2, 4, 4]
result = 0 # Zero is Identity for XOR
for num in nums:
    result ^= num
print(result)  # 3

Why: pairs cancel (x ^ x = 0), leaving the unique element.
"""

# 7b. Find missing number in a sorted array (array 1..n)
"""
def missing_number(nums):
    n = len(nums)
    result = 0 # Zero is Identity for XOR
    for i in range(n+1):
        result ^= i
    for num in nums:
        result ^= num
    return result
"""

# 8. Reverse bits
def reverse_bits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)  # append last bit of n to result
        n >>= 1                     # drop last bit of n
    return result

# 9. Sum of Two integers (Without + and - operators)
def sum_of_ints(a: int, b: int) -> int:
    # 32-bit mask in Python (since Python ints are unbounded)
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0:
        # ^ gets sum without carry
        # & and << gets carry
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # If a is negative, convert from 32-bit unsigned to signed
    return a if a <= MAX_INT else ~(a ^ MASK)

# O(1) - Time complexity -> (at most 32 iterations, since integer is 32-bit)
# O(1) - Space complexity

# 10. Binary Search Algorithm

# Idea -> Minimize some k, such that condition(k) is True
def binary_search(nums: list[int]) -> int:
    # search for minimal k satisfying condition
    def condition(value: int) -> bool:
        pass

    # left, right = min(search_space), max(search_space) 
    left, right = 0, len(nums) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left # return left - 1 -> This is the "minimal k satisfying the condition function"
