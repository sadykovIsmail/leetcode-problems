class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = dict()

        string = list(s)
        print(string)

        for item in string:
            if item in hashmap:
                hashmap[item] = hashmap[item] + 1
            else:
                hashmap[item] = 1

        if min(hashmap.values()) != 1:
            return -1

        least_item = (k for k, v in hashmap.items() if v == min(hashmap.values()))
        
        return string.index(next(least_item))

    
exa = Solution()
print(exa.firstUniqChar("aabb"))