import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums):
        max_num = max(nums)
        present = [False] * (max_num + 1)
        for num in nums:
            present[num] = True
        
        result = 0
        for i in range(1, max_num + 1):
            gcd_value = 0
            for multiple in range(i, max_num + 1, i):
                if present[multiple]:
                    gcd_value = math.gcd(gcd_value, multiple)
                    if gcd_value == i:
                        break
            if gcd_value == i:
                result += 1
        return result
