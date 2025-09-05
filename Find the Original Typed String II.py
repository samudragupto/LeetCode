class Solution:
    MOD = 10**9 + 7

    def possibleStringCount(self, word: str, k: int) -> int:
        groups = []
        n = len(word)
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j
        total = 1
        for group in groups:
            total = (total * group) % self.MOD
        if k <= len(groups):
            return total
        dp = [0] * k
        dp[0] = 1

        for i, group in enumerate(groups):
            new_dp = [0] * k
            window_sum = 0
            for j in range(i, k):
                new_dp[j] = (new_dp[j] + window_sum) % self.MOD
                window_sum = (window_sum + dp[j]) % self.MOD
                if j >= group:
                    window_sum = (window_sum - dp[j - group] + self.MOD) % self.MOD
            
            dp = new_dp
        invalid = sum(dp) % self.MOD
        return (total - invalid + self.MOD) % self.MOD
