# Leetcode 234. Palindrome Linked List

# https://leetcode.com/problems/palindrome-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Use the classic 2-Pointer (slow/fast) solution [Floyd's Tortoise & Hare].

def is_palindrome(head):
    if not head or not head.next:
        return True

    # 1) Find middle (slow ends at middle for odd, at first node of 2nd half for even after step below)
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # If odd length, skip the middle node
    if fast:
        slow = slow.next

    # 2) Reverse second half
    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    second = prev  # head of reversed second half

    # 3) Compare first half and reversed second half
    first = head

    while second:  # only need to traverse the second half
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True

# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity

# Alternative Solution with O(n) Space
# Method -> List Element Equality

def is_palindrome_a(head):
    if not head or not head.next:
        return True

    results = []

    while head:
        results.append(head.val)
        head = head.next
    return results == results[::-1]

# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity