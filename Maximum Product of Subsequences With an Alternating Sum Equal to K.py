from typing import List
from collections import defaultdict
import copy

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        n = len(nums)
        dp = defaultdict(set)

        for i in range(n - 1, -1, -1):
            val = nums[i]
            new_dp = copy.deepcopy(dp)
            if val <= limit:
                new_dp[val].add(val)
            else:
                new_dp[limit + 1].add(val)

            for prod, sums_set in dp.items():
                new_prod = prod * val
                if new_prod > limit:
                    new_prod = limit + 1

                for s in sums_set:
                    new_sum = val - s
                    new_dp[new_prod].add(new_sum)

            dp = new_dp
        dp.pop(limit + 1, None)
        products = sorted(dp.keys(), reverse=True)

        for p in products:
            if k in dp[p]:
                return p
        return -1
