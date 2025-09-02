from collections import defaultdict, deque

class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def topo_sort(conditions):
            graph = defaultdict(list)
            indegree = [0] * (k + 1)
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1

            queue = deque(i for i in range(1, k + 1) if indegree[i] == 0)
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for nxt in graph[node]:
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)

            if len(order) == k:
                return order
            return []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        pos_in_row = {num: i for i, num in enumerate(row_order)}
        pos_in_col = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[pos_in_row[num]][pos_in_col[num]] = num

        return matrix
