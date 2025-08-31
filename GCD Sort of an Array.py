import math
from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootB] = rootA

class Solution:
    def gcdSort(self, nums):
        max_num = max(nums)
        uf = UnionFind(max_num + 1)
        factor_map = defaultdict(list)
        
        for num in set(nums):
            x = num
            f = 2
            while f * f <= x:
                if x % f == 0:
                    factor_map[f].append(num)
                    while x % f == 0:
                        x //= f
                f += 1
            if x > 1:
                factor_map[x].append(num)
        
        for factor, numbers in factor_map.items():
            base = numbers[0]
            for num in numbers[1:]:
                uf.union(base, num)
        
        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if uf.find(a) != uf.find(b):
                return False
        return True
