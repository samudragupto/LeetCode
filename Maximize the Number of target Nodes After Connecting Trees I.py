from typing import List
from collections import deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_graph(n: int, edges: List[List[int]]) -> List[List[int]]:
            g = [[] for _ in range(n)]
            for u, v in edges:
                g[u].append(v)
                g[v].append(u)
            return g
        def count_within_k(start: int, graph: List[List[int]], k_dist: int) -> int:
            if k_dist < 0:
                return 0
            n = len(graph)
            dist = [-1] * n
            q = deque([start])
            dist[start] = 0
            cnt = 1
            while q:
                u = q.popleft()
                if dist[u] == k_dist:
                    continue
                for v in graph[u]:
                    if dist[v] == -1:
                        dist[v] = dist[u] + 1
                        cnt += 1
                        q.append(v)
            return cnt
        n = len(edges1) + 1
        m = len(edges2) + 1
        g1 = build_graph(n, edges1)
        g2 = build_graph(m, edges2)
        cnt1 = [count_within_k(i, g1, k) for i in range(n)]
        cnt2 = [count_within_k(j, g2, k - 1) for j in range(m)]
        max_cnt2 = max(cnt2) if cnt2 else 0
        return [cnt1[i] + max_cnt2 for i in range(n)]
