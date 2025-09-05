import heapq

class Solution:
    def minimumDifference(self, nums):
        n = len(nums) // 3
        min_left_sum = [0] * len(nums)
        max_right_sum = [0] * len(nums)
        max_heap = []
        left_sum = 0
        
        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i]
            
            if len(max_heap) > n:
                left_sum += heapq.heappop(max_heap)
                
            if len(max_heap) == n:
                min_left_sum[i] = left_sum
        min_heap = []
        right_sum = 0
        
        for i in range(len(nums) - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i]
            if len(min_heap) > n:
                right_sum -= heapq.heappop(min_heap)
                
            if len(min_heap) == n:
                max_right_sum[i] = right_sum
        result = float('inf')
        for i in range(n - 1, 2 * n):
            result = min(result, min_left_sum[i] - max_right_sum[i + 1])   
        return result
