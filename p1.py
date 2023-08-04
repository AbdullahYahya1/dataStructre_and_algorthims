from typing import Optional , List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r=  0 ,1 
        maxVal=0
        while True:
            if(prices[r]-prices[l]+1 < 0):
                r+=1 
                l+=1 
                continue
            
            maxVal = max(prices[r]-prices[l] , maxVal )
            r+=1 
            if r == len(prices):
                break
        return maxVal
print(Solution().maxProfit([7,1,5,3,6,4]))