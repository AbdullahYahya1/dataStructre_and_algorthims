from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1 
        maxV = 0
        while l < r:
            d = r-l 
            val=min( height[l] , height[r]) * d
            print(val)
            if maxV < val:
                maxV = val 
            if height[l] < height[r] :
                l+=1 
            elif height[l] >= height[r]:
                r-=1 
        return maxV
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))