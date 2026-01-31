from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.hashSet = set()
        for num in nums:
            if num in self.hashSet:
                return True
            self.hashSet.add(num)
        return False