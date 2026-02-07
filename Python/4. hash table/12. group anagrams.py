from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for st in strs:

            sorted_st = "".join(sorted(st))
            if sorted_st in hashmap.keys():
                hashmap[sorted_st].append(st)
            else:
                hashmap[sorted_st] = [st]
        return list(hashmap.values())


example = Solution()
print(example.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

# exa = 'eat'
# sorted_exa = "".join(sorted(exa))
# hashmap = dict()
# hashmap[sorted_exa] = exa
# exa2 = 'tea'
# sorted_exa2 = "".join(sorted(exa2))
# print()
