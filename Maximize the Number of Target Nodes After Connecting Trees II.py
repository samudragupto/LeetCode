from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def get_parity_counts(n, edges):
            if n == 0:
                return 0, 0, []
            graph = [[] for _ in range(n)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            depth = [-1] * n
            depth[0] = 0
            queue = deque([0])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if depth[v] == -1:
                        depth[v] = depth[u] + 1
                        queue.append(v)
            even = sum(1 for d in depth if d >= 0 and d % 2 == 0)
            odd = n - even
            return even, odd, depth

        n = len(edges1) + 1 if edges1 else 0
        m = len(edges2) + 1 if edges2 else 0
        even1, odd1, depth1 = get_parity_counts(n, edges1)
        even2, odd2, _ = get_parity_counts(m, edges2)
        max_add = max(even2, odd2)
        answer = []
        for i in range(n):
            d = depth1[i]
            if d % 2 == 0:
                answer.append(even1 + max_add)
            else:
                answer.append(odd1 + max_add)
        return answer
