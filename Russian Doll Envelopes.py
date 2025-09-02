from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            i = bisect_left(dp, h)
            if i == len(dp):
                dp.append(h)
            else:
                dp[i] = h
        return len(dp)
