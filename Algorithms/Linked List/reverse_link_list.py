# Leetcode 206. Reverse Linked List

# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    # Iterative solution
    def reverse_list_i(self, head: ListNode):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        
        # # We use 3 pointers: previous, current, next (next_node)
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    # n - number of nodes
    # O(n) - Time complexity
    # O(1) - Space complexity

    # Recursive solution
    def _r_helper(self, prev: ListNode | None, curr: ListNode | None):
        if not curr:
            return prev
        
        next_node = curr.next
        curr.next = prev
        return self._r_helper(curr, next_node)


    def reverse_list_r(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self._r_helper(None, head)
    
    # n - number of nodes
    # O(n) - Time complexity
    # O(n) - Space complexity -> Due to recursion call stack
