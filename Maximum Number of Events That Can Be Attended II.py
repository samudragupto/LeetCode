from functools import lru_cache
import bisect

class Solution:
    def maxValue(self, events, k):
        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == len(events) or remaining == 0:
                return 0
            skip = dp(i+1, remaining)
            end_day = events[i][1]
            val = events[i][2]
            next_i = bisect.bisect_right(starts, end_day)
            attend = val + dp(next_i, remaining - 1)
            
            return max(skip, attend)

        return dp(0, k)
