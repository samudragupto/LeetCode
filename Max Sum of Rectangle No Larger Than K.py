from typing import List
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = float('-inf')
        
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                
                prefix_sums = [0]
                cur_sum = 0
                cur_max = float('-inf')
               
                for val in row_sum:
                    cur_sum += val
                    idx = bisect.bisect_left(prefix_sums, cur_sum - k)
                    if idx < len(prefix_sums):
                        cur_max = max(cur_max, cur_sum - prefix_sums[idx])
                    bisect.insort(prefix_sums, cur_sum)
                
                result = max(result, cur_max)
                
        return result
