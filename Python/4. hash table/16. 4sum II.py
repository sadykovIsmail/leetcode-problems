class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # Step 1: sums of first two arrays
        sum_dict = {}
        for a in nums1:
            for b in nums2:
                s = a + b
                if s in sum_dict:
                    sum_dict[s] += 1
                else:
                    sum_dict[s] = 1

        # Step 2: check sums of last two arrays
        count = 0
        for c in nums3:
            for d in nums4:
                s = c + d
                target = -s
                if target in sum_dict:
                    count += sum_dict[target]

        return count

# Example
sol = Solution()
print(sol.fourSumCount([1,2], [-2,-1], [-1,2], [0,2]))  # Output: 2
