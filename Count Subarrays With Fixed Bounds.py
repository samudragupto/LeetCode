from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        last_min = last_max = -1
        last_invalid = -1

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                last_invalid = i
            if nums[i] == minK:
                last_min = i
            if nums[i] == maxK:
                last_max = i
            valid_length = min(last_min, last_max) - last_invalid
            if valid_length > 0:
                count += valid_length

        return count
