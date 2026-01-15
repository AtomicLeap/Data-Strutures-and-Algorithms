# Leetcode 142 Linked List Cycle II

# https://leetcode.com/problems/linked-list-cycle-ii/description/

class Solution(object):
    def detect_cycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        slow, fast = head, head

        # 1) Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # 2) Find entry
                p1, p2 = head, slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1  # cycle entry

        return None  # no cycle
    
# n - number of nodes
# O(n) - Time complexity
# O(1) - Space complexity