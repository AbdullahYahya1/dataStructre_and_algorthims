from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        while(n):
            n-=1 
            curr=curr.next
            print(n)
        print()
        print()

        while(curr):
            print(curr.val)
            curr=curr.next
        pass 

            


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
    solution.removeNthFromEnd(linked_list , n=1)
    output_list = linked_list_to_list(linked_list)
    print("Input List:", input_list)
    print("Modified List:", output_list)