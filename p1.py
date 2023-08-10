from typing import Optional , List

class Solution:
<<<<<<< HEAD
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(start=0, end=0 , s=''): 
            if(end == n and start == n):
                res.append(s)
                return
            if(start < n) :
                backtrack(start+1 , end , s+'(')
=======
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0 ,  0 
        while True:
            slow=nums[slow] 
            fast=nums[nums[fast]] 
            if(slow==fast):
                break
        
        slow2 = 0

        while(True):
            slow2= nums[slow2]
            slow= nums[slow]
            if slow2 == slow:
                return slow 
>>>>>>> ed456ed668cae2089577914028e4c08a47902217
            

print(Solution().findDuplicate([1,3,4,2,2]))