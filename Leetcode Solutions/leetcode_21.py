# Leetcode 21. Merge Two Sorted Lists

# https://leetcode.com/problems/merge-two-sorted-lists/

# Tags -> Linked list

# ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(list1: list[ListNode], list2: list[ListNode]) -> ListNode:
    head = ListNode()
    current = head
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 or list2
    return head.next


# a, b = [1,2,4], [1,3,4]
# m, n = len(a), len(b)
# l1 = [ListNode(a[i], a[i + 1]) if i < m - 2 else ListNode(a[i]) for i in range(len(a))]
# l2 = [ListNode(b[i], b[i + 1]) if i < n - 2 else ListNode(b[i]) for i in range(len(b))]

print(solution([1,2,4], [1,3,4]))
print(solution([], []))
print(solution([], [0]))