from collections import defaultdict
from typing import List

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        max_state = 3 ** m
        def is_valid(state):
            prev = -1
            for _ in range(m):
                color = state % 3
                if color == prev:
                    return False
                prev = color
                state //= 3
            return True
        def compatible(s1, s2):
            for _ in range(m):
                if (s1 % 3) == (s2 % 3):
                    return False
                s1 //= 3
                s2 //= 3
            return True
        valid = [s for s in range(max_state) if is_valid(s)]
        transitions = {s: [] for s in valid}
        for s1 in valid:
            for s2 in valid:
                if compatible(s1, s2):
                    transitions[s1].append(s2)
        dp = {s: 1 for s in valid}
        for _ in range(1, n):
            new_dp = defaultdict(int)
            for prev, cnt in dp.items():
                for nex in transitions[prev]:
                    new_dp[nex] = (new_dp[nex] + cnt) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD
