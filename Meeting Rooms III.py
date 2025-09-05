import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort(key=lambda x: x[0])
        available = list(range(n))
        heapq.heapify(available)
        occupied = []
        count = [0] * n

        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)

            duration = end - start
            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
                count[room] += 1
            else:
                end_time, room = heapq.heappop(occupied)
                new_start = end_time
                new_end = new_start + duration
                heapq.heappush(occupied, (new_end, room))
                count[room] += 1
        
        max_meetings = max(count)
        return count.index(max_meetings)
