import sys
sys.setrecursionlimit(10**7)

class Solution:
    MOD = 10**9 + 7
    
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        from math import comb
        
        n = len(prevRoom)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[prevRoom[i]].append(i)
        
        fact = [1] * (n + 1)
        for i in range(2, n + 1):
            fact[i] = fact[i-1] * i % self.MOD
        
        def nCr(n, r):
            return fact[n] * pow(fact[r], self.MOD-2, self.MOD) * pow(fact[n-r], self.MOD-2, self.MOD) % self.MOD
        
        def dfs(u):
            total_ways = 1
            total_size = 0
            for v in tree[u]:
                sz, ways = dfs(v)
                total_ways = (total_ways * ways) % self.MOD
                total_ways = (total_ways * nCr(total_size + sz, sz)) % self.MOD
                total_size += sz
            return total_size + 1, total_ways
        
        return dfs(0)[1]
