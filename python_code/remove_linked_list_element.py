
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        extra = ListNode(0)
        extra.next = head
        point = head
        former = extra
        while point:
            if point.val != val:
                former = point
            else:
                former.next = point.next if point.next else None
            point = point.next
        return extra.next