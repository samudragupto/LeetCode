from typing import List
from collections import defaultdict

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        freq = defaultdict(int)
        pairs = 0
        left = 0

        for right in range(n):
            val = nums[right]
            pairs += freq[val]
            freq[val] += 1

            while pairs >= k and left <= right:
                count += n - right
                left_val = nums[left]
                freq[left_val] -= 1
                pairs -= freq[left_val]
                left += 1

        return count
