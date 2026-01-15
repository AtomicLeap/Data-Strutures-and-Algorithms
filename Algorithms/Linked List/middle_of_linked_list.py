# Leetcode 876. Middle of the Linked List

# https://leetcode.com/problems/middle-of-the-linked-list/description/

# This is a classic two-pointer (slow/fast) problem.

class Solution(object):
    def middle_node(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity