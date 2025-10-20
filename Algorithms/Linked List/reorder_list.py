# Leetcode 143. Reorder List

# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reorder_list(head: ListNode) -> None:
    if not head or not head.next or not head.next.next:
        return  # 0,1,2 nodes: already reordered

    # 1) Find middle (slow ends at first-half tail when length is odd)
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 2) Reverse second half starting at slow.next
    prev, curr = None, slow.next
    slow.next = None  # split the list
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    second = prev  # head of reversed second half

    # 3) Merge (weave) first and second halves
    first = head
    while second:
        # Save next pointers
        first_next = first.next
        second_next = second.next
        # Link one from second after one from first
        first.next = second
        second.next = first_next
        # Advance
        first = first_next
        second = second_next
        
# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity