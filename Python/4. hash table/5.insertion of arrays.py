from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        self.hashSet = set(nums1)
        self.result = set()
        for num in nums2:
            if num in self.hashSet:
                self.result.add(num)
            
        result = [num for num in self.result]
        return result
    

    
example = Solution()
print(example.intersection([1, 2, 3, 4, 5], [3, 2, 6, 7, 8, 9]))

#best answer

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
