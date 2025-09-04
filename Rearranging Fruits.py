from collections import Counter

class Solution:
    def minCost(self, basket1, basket2) -> int:
        count = Counter()
        for f in basket1:
            count[f] += 1
        for f in basket2:
            count[f] += 1
        for v in count.values():
            if v % 2 != 0:
                return -1
        
        freq1 = Counter(basket1)
        freq2 = Counter(basket2)
        diff = []
        for fruit in count:
            delta = freq1[fruit] - freq2[fruit]
            if delta > 0:
                diff.extend([fruit] * (delta // 2))
            elif delta < 0:
                diff.extend([fruit] * (-delta // 2))
        
        diff.sort()
        min_fruit = min(count.keys())
        n = len(diff) // 2
        cost = 0
        for i in range(n):
            cost += min(diff[i], 2 * min_fruit)
        
        return cost
