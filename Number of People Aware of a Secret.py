class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        share = 0

        for day in range(2, n + 1):
            start_share = max(0, day - delay)
            stop_share = max(0, day - forget)
            if start_share >= 1:
                share = (share + dp[start_share]) % MOD
            if stop_share >= 1:
                share = (share - dp[stop_share] + MOD) % MOD
            dp[day] = share

        total_know = 0
        for day in range(max(1, n - forget + 1), n + 1):
            total_know = (total_know + dp[day]) % MOD

        return total_know
