class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix_len = len(s)
        suffix_num = int(s)
        power = 10 ** suffix_len
        if suffix_num > finish:
            return 0
        min_num = max(start, suffix_num)
        max_num = finish

        min_prefix = (min_num - suffix_num + power - 1) // power
        max_prefix = (max_num - suffix_num) // power

        def digits(num):
            return list(map(int, str(num)))

        def count_up_to(num_digits, limit):
            from functools import lru_cache

            @lru_cache(None)
            def dfs(pos, restricted, leading_zero):
                if pos == len(num_digits):
                    return 1
                limit_digit = num_digits[pos] if restricted else limit
                total = 0
                for d in range(limit_digit + 1):
                    if d <= limit:
                        total += dfs(pos + 1, restricted and d == limit_digit, leading_zero and d == 0)
                return total

            return dfs(0, True, True)

        def count_range(low, high):
            if low > high:
                return 0
            high_digits = digits(high)
            res_high = count_up_to(high_digits, limit)
            if low == 0:
                return res_high
            low_minus1_digits = digits(low - 1)
            res_low = count_up_to(low_minus1_digits, limit)
            return res_high - res_low

        return count_range(min_prefix, max_prefix)
