from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slwo , fast = head,  head

        while fast and fast.next:
            fast = fast.next.next 
            slwo = slwo.next
            if slwo == fast:
                return True
        return False