import math
import functools

class Solution:
    def maxScore(self, nums):
        n = len(nums) // 2

        @functools.lru_cache(None)
        def dp(k, mask):
            if k == n + 1:
                return 0
            res = 0
            length = len(nums)
            for i in range(length):
                for j in range(i + 1, length):
                    chosenMask = (1 << i) | (1 << j)
                    if (mask & chosenMask) == 0:
                        current_score = k * math.gcd(nums[i], nums[j])
                        res = max(res, current_score + dp(k + 1, mask | chosenMask))
            return res

        return dp(1, 0)
