from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        counter = [0] * len(temperatures)
        stack=[] #[i , temp]
        for i , key in enumerate(temperatures):
            while stack and stack[-1][1] < key:
                index , temp = stack.pop()
                length = i - index 
                counter[index] = length
            stack.append([i , key])
        return counter 
print(Solution().dailyTemperatures([1,2,0,2,4,5]))