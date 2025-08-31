from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        
        result = 0
        
        for i in range(len(points)):
            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0:
                    slope = ('inf', 0)
                else:
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    # Normalize sign: keep dx positive
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                    slope = (dy, dx)
                
                slopes[slope] += 1
            
            current_max = max(slopes.values()) if slopes else 0
            result = max(result, current_max + 1)  # +1 for the point itself
        
        return result
