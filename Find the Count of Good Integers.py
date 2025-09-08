from typing import List
import math

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        half = (n + 1) // 2
        unique_multisets = set()
        start = 10 ** (half - 1)
        end = 10 ** half
        for i in range(start, end):
            first_half = str(i)
            if n % 2 == 0:
                pal_str = first_half + first_half[::-1]
            else:
                pal_str = first_half + first_half[:-1][::-1]
            num = int(pal_str)
            if num % k == 0:
                freq = [0] * 10
                for c in pal_str:
                    freq[int(c)] += 1
                unique_multisets.add(tuple(freq))

        total = 0
        for freq in unique_multisets:
            den_total = 1
            for f in freq:
                den_total *= math.factorial(f)
            total_perm = math.factorial(n) // den_total

            lead_zero_perm = 0
            if freq[0] > 0:
                den_lead = math.factorial(freq[0] - 1)
                for d in range(1, 10):
                    den_lead *= math.factorial(freq[d])
                lead_zero_perm = math.factorial(n - 1) // den_lead

            no_lead = total_perm - lead_zero_perm
            total += no_lead

        return total
