import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.vals.append(val)
        self.idx_map[val].add(len(self.vals) - 1)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.idx_map[val]:
            return False
        remove_idx = self.idx_map[val].pop()
        last_val = self.vals[-1]
        self.vals[remove_idx] = last_val
        self.idx_map[last_val].add(remove_idx)
        self.idx_map[last_val].discard(len(self.vals) - 1)
        self.vals.pop()
        if not self.idx_map[val]:
            del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
