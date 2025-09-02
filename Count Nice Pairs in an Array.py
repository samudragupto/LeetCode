class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        mod = 10**9 + 7

        def rev(x):
            return int(str(x)[::-1])

        count_map = {}
        result = 0
        for x in nums:
            key = x - rev(x)
            if key in count_map:
                result = (result + count_map[key]) % mod
                count_map[key] += 1
            else:
                count_map[key] = 1
        return result
