from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        max_length = 2

        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
                max_length = max(max_length, dp[(i, diff)])

        return max_length
