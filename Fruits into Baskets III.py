from typing import List

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, 2 * node, start, mid)
        self.build(arr, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query_min_index(self, node, start, end, q):
        if self.tree[node] < q:
            return self.n
        if start == end:
            return start
        mid = (start + end) // 2
        left = self.query_min_index(2 * node, start, mid, q)
        if left != self.n:
            return left
        return self.query_min_index(2 * node + 1, mid + 1, end, q)

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        st = SegmentTree(baskets)
        unplaced = 0
        for q in fruits:
            idx = st.query_min_index(1, 0, n - 1, q)
            if idx == n:
                unplaced += 1
            else:
                st.update(1, 0, n - 1, idx, 0)
        return unplaced
