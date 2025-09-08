from typing import List

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & (-idx)

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & (-idx)
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i, val in enumerate(nums2):
            pos2[val] = i

        arr = [pos2[val] for val in nums1]

        fenw_left = FenwickTree(n)
        fenw_mid = FenwickTree(n)

        smaller_left = [0] * n
        for i in range(n):
            smaller_left[i] = fenw_left.query(arr[i] - 1)
            fenw_left.update(arr[i], 1)

        res = 0
        for i in range(n):
            res += fenw_mid.query(arr[i] - 1)
            fenw_mid.update(arr[i], smaller_left[i])

        return res
