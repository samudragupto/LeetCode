class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        N = n + 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = N
        for i in range(n):
            val = nums[i]
            if val < 0:
                val = -val
            if val <= n:
                idx = val - 1
                if nums[idx] > 0:
                    nums[idx] = -nums[idx]
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return N
