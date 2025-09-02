class Solution:
    def minimumPairRemoval(self, nums):
        def is_non_decreasing(arr):
            return all(arr[i] >= arr[i-1] for i in range(1, len(arr)))

        operations = 0
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            idx = 0
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            nums = nums[:idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            operations += 1
        return operations
