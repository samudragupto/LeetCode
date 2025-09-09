from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0
        m = (n + 24) // 25
        @lru_cache(maxsize=None)
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return 0.25 * (dfs(a - 4, b)+dfs(a - 3, b - 1) +dfs(a - 2, b - 2) + dfs(a - 1, b - 3))
        return dfs(m, m)
