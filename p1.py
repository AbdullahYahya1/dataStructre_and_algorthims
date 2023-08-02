from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums= sorted(nums)
        res=[]
        for i , a in enumerate(nums):
            if a > 0:
                break
            if i>0 and a == nums[i-1]:
                continue   
            l , r = i+1 , len(nums)-1
            while l < r: 
                total = nums[l]  + nums[r] + a 

                if total > 0 : 
                    r-=1
                elif total < 0 : 
                    l+=1
                else: 
                    print('here')
                    res.append([ a , nums[l]  , nums[r]])
                    l+=1 
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
print(
Solution().threeSum([0,0,0,0]

))