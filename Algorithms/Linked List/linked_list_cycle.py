# Leetcode 141. Linked List Cycle

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached 
again by continuously following the next pointer. Internally, pos is used to denote the 
index of the node that tail's next pointer is connected to. Note that pos is not passed 
as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 
Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

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