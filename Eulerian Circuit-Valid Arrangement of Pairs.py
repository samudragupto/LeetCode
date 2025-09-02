from collections import defaultdict

class Solution:
    def validArrangement(self, pairs):
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        start = None
        for node in graph:
            if out_degree[node] - in_degree.get(node, 0) == 1:
                start = node
                break
        if start is None:
            start = pairs[0][0]

        stack = [start]
        path = []
        graph_get = graph.get

        while stack:
            curr = stack[-1]
            edges = graph_get(curr)
            if edges:
                stack.append(edges.pop())
            else:
                path.append(stack.pop())

        path.reverse()
        return [[path[i], path[i+1]] for i in range(len(path)-1)]
