import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while heap:
            time, r, c = heapq.heappop(heap)
            if time > dist[r][c]:
                continue
            if r == m - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_time = max(time + 1, moveTime[nr][nc] + 1)
                    if new_time < dist[nr][nc]:
                        dist[nr][nc] = new_time
                        heapq.heappush(heap, (new_time, nr, nc))
        return -1
