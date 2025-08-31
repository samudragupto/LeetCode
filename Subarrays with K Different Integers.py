class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.atMostKDistinct(nums, k) - self.atMostKDistinct(nums, k - 1)

    def atMostKDistinct(self, nums, k):
        count = {}
        left = 0
        result = 0
        
        for right in range(len(nums)):
            count[nums[right]] = count.get(nums[right], 0) + 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            result += right - left + 1
        
        return result
