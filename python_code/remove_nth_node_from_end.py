
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        end = dummy
        internal = 0
        while start.next:
            start = start.next
            internal += 1
            if internal >= n + 1:
                end = end.next
        if internal == n:
            return dummy.next.next
        end.next = end.next.next
        return dummy.next