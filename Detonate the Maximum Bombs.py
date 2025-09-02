from collections import deque

class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx * dx + dy * dy <= r1 * r1:
                    graph[i].append(j)

        def bfs(start):
            visited = set([start])
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            return len(visited)

        max_detonated = 1
        for i in range(n):
            max_detonated = max(max_detonated, bfs(i))
        return max_detonated
