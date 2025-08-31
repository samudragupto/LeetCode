class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

class Solution:
    def areConnected(self, n, threshold, queries):
        uf = UnionFind(n)

        # Union multiples of every number greater than threshold
        for divisor in range(threshold + 1, n + 1):
            multiple = 2 * divisor
            while multiple <= n:
                uf.union(divisor, multiple)
                multiple += divisor

        # Process queries
        result = []
        for a, b in queries:
            result.append(uf.find(a) == uf.find(b))
        return result
