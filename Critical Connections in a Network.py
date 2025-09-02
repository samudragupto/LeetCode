class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        self.time = 0
        disc = [-1] * n
        low = [0] * n
        res = []
        def dfs(u, parent):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            for v in graph[u]:
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u, v])
                elif v != parent:
                    low[u] = min(low[u], disc[v])
        dfs(0, -1)
        return res
