from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max = 0 
        cur = 0
        
        for num in nums:
            if num == 1:
                cur += 1
                max = max if max > cur else cur
            else:
                cur = 0
                
        return max
    
    
sol = Solution()
print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))