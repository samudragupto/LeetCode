from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort_count(a, l, r):
            if r - l <= 1:
                return 0
            m = (l + r) // 2
            cnt = sort_count(a, l, m) + sort_count(a, m, r)

            j = m
            for i in range(l, m):
                while j < r and a[i] > 2 * a[j]:
                    j += 1
                cnt += j - m

            temp = []
            i, j = l, m
            while i < m and j < r:
                if a[i] <= a[j]:
                    temp.append(a[i]); i += 1
                else:
                    temp.append(a[j]); j += 1
            temp.extend(a[i:m])
            temp.extend(a[j:r])
            a[l:r] = temp
            return cnt

        return sort_count(nums, 0, len(nums))
