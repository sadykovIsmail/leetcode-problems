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


# how it should be
from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # Check if left sum equals right sum
            if left_sum == (total_sum - left_sum - num):
                return i
            left_sum += num
        
        return -1

