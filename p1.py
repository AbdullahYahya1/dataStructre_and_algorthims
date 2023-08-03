from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #SPLIT
        slow , fast = head , head.next
        while(fast and fast.next):
            slow = slow.next
            fast=fast.next.next 
        half=slow.next
        slow.next=None


        #TAKE OPSIT 
        curr , pre= half , None
        while(curr):
            swap=curr.next
            curr.next=pre
            pre=curr
            curr=swap

        #it is opesit and stored in half 
        #now we will mearge them to make new arr 
        curr , half = head , pre 
        while(half):
            swap = curr.next
            swaph = half.next
            curr.next=half
            half.next= swap
            curr=swap
            half=swaph
            


# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy_head = ListNode()
    current = dummy_head
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    linked_list = list_to_linked_list(input_list)
    solution = Solution()
    solution.reorderList(linked_list)
    output_list = linked_list_to_list(linked_list)
    print("Input List:", input_list)
    print("Modified List:", output_list)