from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = dict()
        total = 0

        for i, num in enumerate(nums):
            if num in hashmap:
                if num < 0:
                    total = abs(hashmap[num] + i)
                else:
                     total = abs(hashmap[num] - i)
                if total <= k:
                    return True
                else:
                    del hashmap[num]
            hashmap[num] = i
        return False




example = Solution()
print(example.containsNearbyDuplicate([1,2,3,1,2,3], 2))


"""
cleanest version
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False

"""