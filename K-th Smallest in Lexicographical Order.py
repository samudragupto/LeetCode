class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_prefix(prefix, n):
            cur = prefix
            nxt = prefix + 1
            count = 0
            while cur <= n:
                count += min(n + 1, nxt) - cur
                cur *= 10
                nxt *= 10
            return count
        
        curr = 1
        k -= 1
        while k > 0:
            cnt = count_prefix(curr, n)
            if cnt <= k:
                curr += 1
                k -= cnt
            else:
                curr *= 10
                k -= 1
        return curr
