from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            if num in nums2:
                result.append(num)
                nums2.remove(num)
        

        return result
    
example = Solution()
print(example.intersect([1, 2, 2, 1], [2]))

#faster version
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        result = []

        for num in c1:
            if num in c2:
                times = min(c1[num], c2[num])
                result.extend([num] * times)

        return result
