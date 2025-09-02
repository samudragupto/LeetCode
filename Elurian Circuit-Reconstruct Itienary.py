from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dest in tickets:
            graph[src].append(dest)

        for src in graph:
            graph[src].sort(reverse=True)

        route = []

        def visit(airport):
            while graph[airport]:
                next_dest = graph[airport].pop()
                visit(next_dest)
            route.append(airport)

        visit("JFK")
        return route[::-1]
