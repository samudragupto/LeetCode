import math

class Solution:
    def minStable(self, nums, maxC):
        n = len(nums)
        
        single_count = sum(1 for x in nums if x >= 2)
        if maxC >= single_count:
            return 0
        
        LOG = n.bit_length()
        st = [[0]*n for _ in range(LOG)]
        for i in range(n):
            st[0][i] = nums[i]
        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1
            for i in range(n - length + 1):
                st[j][i] = math.gcd(st[j-1][i], st[j-1][i+half])
            j += 1

        def range_gcd(l, r):
            k = (r-l+1).bit_length() - 1
            return math.gcd(st[k][l], st[k][r - (1<<k) + 1])

        def can(K):
            if K >= n:
                return True
                
            modifications = 0
            i = 0
            
            while i <= n - K - 1:
                if range_gcd(i, i + K) >= 2:
                    modifications += 1
                    if modifications > maxC:
                        return False
                    i += K + 1
                else:
                    i += 1
                    
            return True

        lo, hi, ans = 1, n, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
                
        return ans
