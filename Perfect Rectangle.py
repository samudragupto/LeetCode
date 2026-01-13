from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if not rectangles:
            return False
        
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        area = 0
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            area += (x2 - x1) * (y2 - y1)
            
            for p in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if p in corners:
                    corners.remove(p)
                else:
                    corners.add(p)
        
        if area != (max_x - min_x) * (max_y - min_y):
            return False
        
        expected = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        return corners == expected
