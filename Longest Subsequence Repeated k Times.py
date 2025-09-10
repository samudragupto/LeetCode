from typing import List
from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = Counter(s)
        chars = [c for c in freq if freq[c] >= k]
        chars.sort(reverse=True)

        def can_form(t):
            i = 0
            for _ in range(k):
                for ch in t:
                    i = s.find(ch, i) + 1
                    if i == 0:
                        return False
            return True

        ans = ""
        queue = deque([""])
        while queue:
            cand = queue.popleft()
            for c in chars:
                nxt = cand + c
                if can_form(nxt):
                    if len(nxt) > len(ans) or (len(nxt) == len(ans) and nxt > ans):
                        ans = nxt
                    queue.append(nxt)
        return ans
