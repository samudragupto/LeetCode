import math
import functools
from collections import Counter, defaultdict

class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        def is_square(x):
            r = int(math.isqrt(x))
            return r * r == x

        n = len(nums)
        count = Counter(nums)
        graph = defaultdict(list)

        unique_nums = list(count.keys())
        for i in unique_nums:
            for j in unique_nums:
                if is_square(i + j):
                    graph[i].append(j)

        @functools.lru_cache(None)
        def dfs(x, remaining):
            total_remaining = sum(freq for _, freq in remaining)
            if total_remaining == 0:
                return 1
            total = 0
            remaining_dict = dict(remaining)
            for y in graph[x]:
                if remaining_dict.get(y, 0) > 0:
                    remaining_dict[y] -= 1
                    if remaining_dict[y] == 0:
                        del remaining_dict[y]
                    total += dfs(y, frozenset(remaining_dict.items()))
                    remaining_dict[y] = remaining_dict.get(y, 0) + 1
            return total

        total_perms = 0
        for num in unique_nums:
            c = dict(count)
            c[num] -= 1
            if c[num] == 0:
                del c[num]
            total_perms += dfs(num, frozenset(c.items()))

        return total_perms
