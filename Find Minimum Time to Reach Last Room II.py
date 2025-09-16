import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        pq = [(0, 0, 0, 0)]
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while pq:
            time, x, y, parity = heapq.heappop(pq)
            
            if (x, y, parity) in visited:
                continue
            visited.add((x, y, parity))
            
            if x == n - 1 and y == m - 1:
                return time
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    move_cost = 1 if parity == 0 else 2
                    start_time = max(time, moveTime[nx][ny])
                    next_time = start_time + move_cost
                    next_parity = 1 - parity
                    
                    if (nx, ny, next_parity) not in visited:
                        heapq.heappush(pq, (next_time, nx, ny, next_parity))
        
        return -1
