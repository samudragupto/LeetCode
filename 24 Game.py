from typing import List
import math

class Solution:
    def _dfs(self, nums: List[float]) -> bool:
        if len(nums) == 1:
            return math.isclose(nums[0], 24.0, abs_tol=1e-6)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                a, b = nums[i], nums[j]
                rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                for val in (a + b,
                            a - b, b - a,
                            a * b,
                            a / b if b != 0 else None,
                            b / a if a != 0 else None):
                    
                    if val is None:
                        continue
                    if self._dfs(rest + [val]):
                        return True
        return False
    def judgePoint24(self, cards: List[int]) -> bool:
        return self._dfs([float(x) for x in cards])
