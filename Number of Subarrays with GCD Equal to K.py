import math
from typing import List

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = math.gcd(g, nums[j])
                if g == k:
                    count += 1
                elif g < k:
                    break  # GCD won't increase later, so break early
                    
        return count
