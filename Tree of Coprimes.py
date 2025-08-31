import math
from collections import defaultdict

class Solution:
    def getCoprimes(self, nums, edges):
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        coprimes = [[] for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if math.gcd(i, j) == 1:
                    coprimes[i].append(j)

        ans = [-1] * n
        stacks = defaultdict(list)

        def dfs(node, parent, depth):
            val = nums[node]
            max_depth = -1
            ancestor = -1

            for c in coprimes[val]:
                if stacks[c]:
                    if stacks[c][-1][1] > max_depth:
                        max_depth = stacks[c][-1][1]
                        ancestor = stacks[c][-1][0]

            ans[node] = ancestor

            stacks[val].append((node, depth))

            for nei in adj[node]:
                if nei != parent:
                    dfs(nei, node, depth + 1)

            stacks[val].pop()

        dfs(0, -1, 0)
        return ans
