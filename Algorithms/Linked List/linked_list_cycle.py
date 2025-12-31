# Leetcode 141. Linked List Cycle

# https://leetcode.com/problems/linked-list-cycle/description/

# Idea
# Floyd’s Cycle Detection Algorithm (also called the Tortoise and Hare algorithm)
# We use two pointers:
# slow moves one step at a time
# fast moves two steps at a time
# Key idea:
# If there’s no cycle, fast will reach None (end of list).
# If there is a cycle, the two pointers will eventually meet inside the cycle.
# This works like two runners on a circular track — the faster one will eventually “lap” the slower one.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next          
        fast = fast.next.next     
        
        if slow == fast:          # pointers meet → cycle detected
            return True
    
    return False                 

# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity

# Alternative solution with O(n) Space
def has_cycle_n(head):
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False

# n - number of nodes
# O(n) - Time complexity
# O(n) - Space complexity