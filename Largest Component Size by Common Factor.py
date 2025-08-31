from collections import defaultdict
import math

class Solution:
    def largestComponentSize(self, nums):
        n = len(nums)
        
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
            
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
        
        uf = UnionFind(n)
        factor_map = {}
        
        def find_factors(num):
            factors = set()
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    factors.add(i)
                    factors.add(num // i)
            factors.add(num)
            return factors
        
        for i, num in enumerate(nums):
            factors = find_factors(num)
            for f in factors:
                if f in factor_map:
                    uf.union(i, factor_map[f])
                factor_map[f] = i
        
        count = defaultdict(int)
        max_size = 0
        for i in range(n):
            root = uf.find(i)
            count[root] += 1
            max_size = max(max_size, count[root])
        
        return max_size
