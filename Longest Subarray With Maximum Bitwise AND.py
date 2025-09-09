from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = max(nums)
        longest = 0
        current_len = 0

        for num in nums:
            if num == max_val:
                current_len += 1
                longest = max(longest, current_len)
            else:
                current_len = 0

        return longest
