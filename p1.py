from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(start=0, end=0 , s=''): 
            if(end == n and start == n):
                res.append(s)
                return
            if(start < n) :
                backtrack(start+1 , end , s+'(')
            
            if(end < start):
                backtrack(start , end+1 , s+')')
        backtrack()
        return res 
print( Solution().generateParenthesis(3))