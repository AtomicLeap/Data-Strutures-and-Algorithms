# Leetcode 2. Add Two Numbers

# https://leetcode.com/problems/add-two-numbers/description/

# Tags -> Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10
            
            current.next = ListNode(total % 10)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    
# Let n = len(l1), m = len(l2)
# O(max(n, m)) - Time complexity
# O(max(n, m)) - Space complexity