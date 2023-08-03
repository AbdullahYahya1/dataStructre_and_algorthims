from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dic={}
        cur = head
        while cur :
            dic[cur] = Node(x=cur.val)
            cur=cur.next
        cur = head
        while cur :
            dic[cur].random=dic[cur.random] if cur.random else None  
            dic[cur].next=dic[cur.next] if cur.next else None 
            cur=cur.next
        
        return dic[head]
        