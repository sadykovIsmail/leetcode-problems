class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        hashset = dict()
        result = 0
        best = 0
        two = 0
        List = list(s)

        for i, c in enumerate(List):
            if c not in hashset.values():
                result += 1
                hashset[i] = c

            else:
                if result > best:
                    best = result
                index = next((k for k, v in hashset.items() if v == c))


                for key in list(hashset.keys()):
                    if key <= index:
                        del hashset[key]
                hashset[i] = c
                result = len(hashset)

            two += 1
        if result > best:
            best = result
        return best

exa = Solution()
print(exa.lengthOfLongestSubstring("dvdf"))

"""What we needed
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}   # character -> last index
        left = 0         # left pointer of window
        max_len = 0

        for right, char in enumerate(s):
            # If we have seen the character and it's inside current window
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            # Update last seen index
            last_seen[char] = right

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len

"""