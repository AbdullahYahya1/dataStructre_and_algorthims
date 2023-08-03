from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        newList = ListNode()
        currRes = newList
        remindr = 0

        while curr1 or curr2 or remindr:
            val = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + remindr
            remindr = val // 10
            val = val % 10
            currRes.next = ListNode(val)
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
            currRes = currRes.next

        return newList.next