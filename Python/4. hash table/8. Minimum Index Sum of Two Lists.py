from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = dict()
      
        for i, a in enumerate(list1):
            if a in list2:
                j = list2.index(a)  # find index in list2
                sum_index = i + j
                if sum_index in result:
                    result[sum_index].append(a)
                else:
                    result[sum_index] = [a]

        if not result:  # edge case: no common restaurant
            return []

        min_sum = min(result.keys())
        return result[min_sum]
