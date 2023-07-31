from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack =[]
        arr=sorted(list(zip(position , speed)) , reverse=True)
        for position , speed in arr:
            t= (float(target-position)/float(speed))
            if stack and stack[-1]>=t:
                pass 
            else: 
                stack.append(t)
                
        return len(stack) 
print(Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))