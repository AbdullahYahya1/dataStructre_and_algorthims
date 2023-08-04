class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r =  0 , 0
        seen=set()
        maxS=0
        n =len(s)
        while(r  < n):
            while(s[r] in seen):
                seen.discard(s[l])
                l +=1  
            seen.add(s[r])
            r+=1 
            maxS = max(maxS ,len(seen))
        return maxS