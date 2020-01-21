# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        carry = 0 
        firstNode = None
        Nodes = None
        times = 1
        while l1 or l2 or carry != 0:
            val = (l1.var if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val // 10
            mode = val % 10
            node = ListNode(mode)
            if times == 1:
                firstNode = node
                times = 0
            else:
                Nodes.next = node
            
            Nodes = node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return firstNode

  

                


