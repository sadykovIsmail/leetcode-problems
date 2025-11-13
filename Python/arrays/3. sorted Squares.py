from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        
        for num in nums:
            result.append(num * num)
            
        result.sort()
        return result
    
    
sol = Solution()

print(sol.sortedSquares([-5, -4, -3, 2, 4]))