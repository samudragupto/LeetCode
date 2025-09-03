MOD = 10**9 + 7

class Solution:
    def countOfPairs(self, nums):
        n = len(nums)
        maxv = max(nums)
        dp = [ [0] * (maxv+1) for _ in range(n) ]
        for a in range(nums[0]+1):
            dp[0][a] = 1

        for i in range(1, n):
            for a in range(nums[i]+1):
                for prev_a in range(nums[i-1]+1):
                    if prev_a <= a and nums[i-1] - prev_a >= nums[i] - a:
                        dp[i][a] = (dp[i][a] + dp[i-1][prev_a]) % MOD

        return sum(dp[n-1][a] for a in range(nums[n-1]+1)) % MOD
