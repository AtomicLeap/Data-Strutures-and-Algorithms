# Leetcode 19. Remove Nth Node From End of List

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Idea -> One Pass
def remove_nth_node(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy

    # 1) Advance fast n steps
    for _ in range(n):
        fast = fast.next

    # 2) Move both until fast is at the last node
    while fast.next:
        fast = fast.next
        slow = slow.next

    # 3) Remove slow.next
    slow.next = slow.next.next
    return dummy.next

# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity

# Idea -> Two Pass
# First pass: find length of list.
# Second pass: Find the node before the one to delete
def remove_nth_node2(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)

    # First pass: find length of list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Second pass: Find the node before the one to delete
    current = dummy
    for _ in range(length - n):
        current = current.next

    # Remove the nth node from end
    current.next = current.next.next

    return dummy.next

# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity
