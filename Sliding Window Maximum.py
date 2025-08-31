from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []
        
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            
            if dq[0] == i - k:
                dq.popleft()
            
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
