# Leetcode 23. Merge k Sorted Lists

# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Using Heap Priority Queue
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next
    def __repr__(self):  # for debugging
        return f"{self.val}->{self.next}"


def merge_k_lists_h(lists: list[ListNode] | None) -> ListNode | None:
    heap = []
    # Push the head of each non-empty list: (value, unique_id, node)
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))  # i breaks ties

    dummy = ListNode()
    tail = dummy

    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next

# n - number of nodes, k - number of lists
# O(n.log k) - Time complexity
# O(k) - Space complexity

# Divide and Conquer solution
def merge_k_lists_d(lists: list[ListNode] | None) -> ListNode | None:
    if not lists:
        return None
    interval = 1
    while interval < len(lists):
        for i in range(0, len(lists) - interval, interval * 2):
            lists[i] = merge_two(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]

def merge_two(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next

# n - number of nodes, k - number of lists
# O(n.log k) - Time complexity
# O(1) - Space complexity (Besides Recursion call stack)