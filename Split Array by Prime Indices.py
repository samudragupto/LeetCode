class Solution:
    def splitArray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        is_prime = [False, False] + [True] * (n - 2)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        sum_a = 0
        sum_b = 0
        for i in range(n):
            if is_prime[i]:
                sum_a += nums[i]
            else:
                sum_b += nums[i]

        return abs(sum_a - sum_b)
