from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=''
        n2=''
        curr=l1
        while l1:
            n1+=str(l1.val)
            l1 = l1.next
        curr=l2
        while l2:
            n2+=str(l2.val)
            l2 = l2.next
        n = str(int(n1[::-1])+int(n2[::-1]))
        n = n[::-1]
        head = ListNode()
        curr= head
        for c in n :
            curr.next = ListNode(val=int(c))
            curr=curr.next
        return head.next       