from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        copy = nums.copy()
        copy.sort()
        
        print(nums, copy)
        if copy[len(copy) - 2] * 2 <= copy[len(copy) - 1]:
            re =  nums.index(copy[len(copy) - 1])
            return re
        else:
            return -1
        
        

example = Solution()
print(example.dominantIndex([3,6,1,0]))