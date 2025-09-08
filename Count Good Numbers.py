class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_pos = (n + 1) // 2
        odd_pos = n // 2

        def mod_pow(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result

        return (mod_pow(5, even_pos, MOD) * mod_pow(4, odd_pos, MOD)) % MOD
