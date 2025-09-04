from collections import defaultdict

class Solution:
    def minimumScore(self, nums, edges):
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [-1] * n
        subtree_xor = [0] * n
        subtree_size = [1] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        def dfs(node, par):
            nonlocal time
            parent[node] = par
            time += 1
            in_time[node] = time
            xor_val = nums[node]
            for neigh in graph[node]:
                if neigh != par:
                    xor_val ^= dfs(neigh, node)
                    subtree_size[node] += subtree_size[neigh]
            subtree_xor[node] = xor_val
            time += 1
            out_time[node] = time
            return xor_val

        dfs(0, -1)
        total_xor = subtree_xor[0]

        edge_list = []
        for u, v in edges:
            if parent[u] == v:
                edge_list.append((v, u))
            else:
                edge_list.append((u, v))

        def is_ancestor(u, v):
            return in_time[u] <= in_time[v] and out_time[u] >= out_time[v]

        ans = float('inf')
        m = len(edge_list)
        for i in range(m):
            p1, c1 = edge_list[i]
            for j in range(i + 1, m):
                p2, c2 = edge_list[j]

                if is_ancestor(c1, c2):
                    a = subtree_xor[c2]
                    b = subtree_xor[c1] ^ a
                    c = total_xor ^ subtree_xor[c1]
                elif is_ancestor(c2, c1):
                    a = subtree_xor[c1]
                    b = subtree_xor[c2] ^ a
                    c = total_xor ^ subtree_xor[c2]
                else:
                    a = subtree_xor[c1]
                    b = subtree_xor[c2]
                    c = total_xor ^ a ^ b

                max_val = max(a, b, c)
                min_val = min(a, b, c)
                ans = min(ans, max_val - min_val)

        return ans
