class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for _ in range(n)]
        total = 0
        for i in range(n):
            di = dp[i]
            ni = nums[i]
            for j in range(i):
                diff = ni - nums[j]
                cnt = dp[j].get(diff, 0)
                di[diff] = di.get(diff, 0) + cnt + 1
                total += cnt
        return total
