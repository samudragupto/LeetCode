class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        total_area = 0
        for x, y, l in squares:
            total_area += l * l
            events.append((y, l))
            events.append((y + l, -l))
        
        target = total_area / 2.0
        
        events.sort(key=lambda e: (e[0], -e[1]))
        
        cum_area = 0.0
        active = 0
        j = 0
        n_events = len(events)
        if n_events == 0:
            return 0.0
        
        prev_y = events[0][0]
        
        while j < n_events:
            curr_y = events[j][0]
            dist = curr_y - prev_y
            
            if dist > 0 and active > 0:
                area_add = active * dist
                if cum_area + area_add >= target:
                    needed = target - cum_area
                    length = needed / active
                    return prev_y + length
                cum_area += area_add
            
            while j < n_events and events[j][0] == curr_y:
                active += events[j][1]
                j += 1
            
            prev_y = curr_y
        
        return float(prev_y)
