from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self.hashSet = set()
        for num in nums :
            if num in self.hashSet:
                self.hashSet.remove(num)
            else:

                self.hashSet.add(num)

        return self.hashSet.pop()
    
examples = Solution()
print(examples.singleNumber([1, 2, 4, 1, 2, 4, 5]))