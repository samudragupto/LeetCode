from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        has_key = [False] * n
        found_boxes = set(initialBoxes)
        queue = deque()
        visited = [False] * n
        total = 0
        for box in list(found_boxes):
            if status[box] == 1 and not visited[box]:
                queue.append(box)
                visited[box] = True

        while queue:
            box = queue.popleft()
            total += candies[box]

            for k in keys[box]:
                has_key[k] = True
                if k in found_boxes and not visited[k]:
                    queue.append(k)
                    visited[k] = True

            for cb in containedBoxes[box]:
                found_boxes.add(cb)
                if (status[cb] == 1 or has_key[cb]) and not visited[cb]:
                    queue.append(cb)
                    visited[cb] = True

        return total
