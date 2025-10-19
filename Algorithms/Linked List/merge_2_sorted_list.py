# Leetcode 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution
def merge_two_listsi(list1: ListNode, list2: ListNode) -> ListNode:
    # Step 1: Dummy node
    dummy = ListNode(-1)
    tail = dummy
    
    # Step 2: Traverse both lists
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    # Step 3: Attach remaining nodes
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    # Step 4: Return merged list (skip dummy)
    return dummy.next

# O(n + m) - Time complexity -> Traverse both lists once
# O(1) - Space complexity

# Recursive solution
def merge_two_listsr(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    if not list2:
        return list1
    
    if list1.val < list2.val:
        list1.next = merge_two_listsr(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_listsr(list1, list2.next)
        return list2

# O(n + m) - Time complexity -> Traverse both lists once
# O(n + m) - Space complexity -> Due to recursion call stack