from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        firstPlayer -= 1
        secondPlayer -= 1
        
        @lru_cache(None)
        def dfs(mask, p1, p2):
            players = [i for i in range(n) if mask & (1 << i)]
            length = len(players)           
            pos1 = players.index(p1)
            pos2 = players.index(p2)
            if pos1 + pos2 == length - 1:
                return (1, 1)
            
            earliest = float('inf')
            latest = -float('inf')
            pairs = []
            for i in range(length // 2):
                pairs.append((players[i], players[length - 1 - i]))
            if length % 2 == 1:
                pairs.append((players[length // 2],))
            
            def backtrack(i, winners):
                nonlocal earliest, latest
                if i == len(pairs):
                    new_mask = 0
                    for w in winners:
                        new_mask |= (1 << w)
                    e, l = dfs(new_mask, p1, p2)
                    earliest = min(earliest, e + 1)
                    latest = max(latest, l + 1)
                    return
                pair = pairs[i]
                if len(pair) == 1:
                    backtrack(i + 1, winners + [pair[0]])
                else:
                    a, b = pair
                    if a == p1 or a == p2:
                        backtrack(i + 1, winners + [a])
                    elif b == p1 or b == p2:
                        backtrack(i + 1, winners + [b])
                    else:
                        backtrack(i + 1, winners + [a])
                        backtrack(i + 1, winners + [b])
            
            backtrack(0, [])
            return (earliest, latest)
        
        full_mask = (1 << n) - 1
        return dfs(full_mask, firstPlayer, secondPlayer)
