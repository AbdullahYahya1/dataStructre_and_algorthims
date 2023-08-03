from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        curr=head
        while(n>0):
            n-=1
            curr=curr.next
        pre =dummy_head
        while(curr):
            curr=curr.next
            pre=pre.next
        pre.next=pre.next.next
        return dummy_head.next
