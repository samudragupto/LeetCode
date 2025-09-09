from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last_set = [-1] * 32

        for i in range(n - 1, -1, -1):
            num = nums[i]
            for bit in range(32):
                if num & (1 << bit):
                    last_set[bit] = i

            max_idx = i
            for bit in range(32):
                if last_set[bit] != -1:
                    max_idx = max(max_idx, last_set[bit])

            answer[i] = max_idx - i + 1

        return answer
