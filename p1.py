class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= [char.lower() for char in s if char.isalnum()]
        if not s:
            return True
        left ,right= 0 , len(s)-1
        while left<=right:
            if (s[left] != s[right]):
                return False
            left+=1
            right-=1
        return True
print(Solution().isPalindrome('A man, a plan, a canal: Panama'))