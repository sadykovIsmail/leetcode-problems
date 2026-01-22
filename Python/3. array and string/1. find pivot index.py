from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        point = 0
        
        while len(nums) - 1 > point:
            if sum(nums[:point]) == sum(nums[point+1:]):
                return point
            point += 1
        if sum(nums[:point]) == sum(nums[point+1:]):
                return point
        elif sum(nums[:point]) != sum(nums[point+1:]):
            
            return -1
            
    
example = Solution()
print(example.pivotIndex([2]))