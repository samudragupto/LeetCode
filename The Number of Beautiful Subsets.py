class Solution:
    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0

        def backtrack(i, chosen):
            nonlocal count
            if i == n:
                if chosen:
                    count += 1
                return
            backtrack(i + 1, chosen)
            for x in chosen:
                if abs(nums[i] - x) == k:
                    return 
            backtrack(i + 1, chosen + [nums[i]])

        backtrack(0, [])
        return count
