from itertools import combinations
from math import gcd, comb
from collections import Counter
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slopes = Counter()
        lines = Counter()
        mids = Counter()
        midlines = Counter()

        for (x1, y1), (x2, y2) in combinations(points, 2):
            dx, dy = x2 - x1, y2 - y1
            g = gcd(dx, dy)
            dx //= g
            dy //= g
            if dx < 0 or (dx == 0 and dy < 0):
                dx = -dx
                dy = -dy
            inter = dx * y1 - dy * x1
            slopes[(dx, dy)] += 1
            lines[(dx, dy, inter)] += 1
            mids[x1 + x2, y1 + y2] += 1
            midlines[(x1 + x2, y1 + y2, dx, dy, inter)] += 1
        total = sum(comb(v, 2) for v in slopes.values())
        subtract_lines = sum(comb(v, 2) for v in lines.values())
        subtract_mids = sum(comb(v, 2) for v in mids.values())
        add_midlines = sum(comb(v, 2) for v in midlines.values())
        return total - subtract_lines - subtract_mids + add_midlines
