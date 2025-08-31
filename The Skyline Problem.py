import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))
        
        events.sort()
        result = []
        heap = [(0, float('inf'))]
        prev_height = 0
        
        for x, negH, R in events:
            while heap[0][1] <= x:
                heapq.heappop(heap)
            if negH != 0:
                heapq.heappush(heap, (negH, R))
            current_height = -heap[0][0]
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height
        
        return result
