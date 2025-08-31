import math
from collections import Counter

class Solution:
    def countPairs(self, nums, k):
        gcd_count = Counter()
        for num in nums:
            g = math.gcd(num, k)
            gcd_count[g] += 1

        keys = list(gcd_count.keys())
        result = 0

        for i, g1 in enumerate(keys):
            for j in range(i, len(keys)):
                g2 = keys[j]
                if (g1 * g2) % k == 0:
                    if i == j:
                        count = gcd_count[g1]
                        result += count * (count - 1) // 2
                    else:
                        result += gcd_count[g1] * gcd_count[g2]

        return result
