# Leetcode 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/

# Data structure -> Linked list

# LeetCode-style ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(list1: list[ListNode], list2: list[ListNode]) -> ListNode:
    dummy = tail = ListNode()
    a, b = list1, list2
    while a and b:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


# a, b = [1,2,4], [1,3,4]
# m, n = len(a), len(b)
# l1 = [ListNode(a[i], a[i + 1]) if i < m - 2 else ListNode(a[i]) for i in range(len(a))]
# l2 = [ListNode(b[i], b[i + 1]) if i < n - 2 else ListNode(b[i]) for i in range(len(b))]

print(solution([1,2,4], [1,3,4]))
print(solution([], []))
print(solution([], [0]))