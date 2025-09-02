class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = []
        total = k ** n

        def dfs(node):
            for x in map(str, range(k)):
                nxt = node + x
                if nxt not in seen:
                    seen.add(nxt)
                    dfs(nxt[1:])
                    ans.append(x)

        start = "0" * (n - 1)
        dfs(start)
        return "".join(ans) + start
