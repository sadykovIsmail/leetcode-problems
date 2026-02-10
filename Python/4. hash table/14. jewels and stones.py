class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        for s in list(stones):
            if s in list(jewels):
                result += 1
        return result

exa = Solution()

print(exa.numJewelsInStones("aA", "aAAbbbb"))