from typing import List
import bisect

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_leq(x):
            count = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        count += len(nums2)
                elif a > 0:
                    idx = bisect.bisect_right(nums2, x // a)
                    count += idx
                else:
                    val = x / a
                    idx = bisect.bisect_left(nums2, val)
                    count += len(nums2) - idx
            return count

        left, right = -10**15, 10**15
        while left < right:
            mid = (left + right) // 2
            if count_leq(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
