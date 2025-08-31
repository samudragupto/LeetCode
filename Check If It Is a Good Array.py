import math
from functools import reduce

class Solution:
    def isGoodArray(self, nums):
        gcd_value = reduce(math.gcd, nums)
        return gcd_value == 1
