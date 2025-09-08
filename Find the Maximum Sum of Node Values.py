from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        base = sum(nums)
        deltas = [(nums[i] ^ k) - nums[i] for i in range(n)]
        pos = [d for d in deltas if d > 0]
        neg_or_zero = [d for d in deltas if d <= 0]
        sumP = sum(pos)
        cntP = len(pos)
        if cntP % 2 == 0:
            return base + sumP
        drop_pos = sumP - (min(pos) if pos else 0)
        add_neg = sumP + (max(neg_or_zero) if neg_or_zero else float('-inf'))
        best_gain = max(drop_pos, add_neg)
        return base + best_gain
