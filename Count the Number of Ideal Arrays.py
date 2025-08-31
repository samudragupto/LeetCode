MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n, maxValue):
        max_prime = maxValue
        primes = []
        is_prime = [True] * (max_prime + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, max_prime + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i*i, max_prime + 1, i):
                    is_prime[j] = False

        def prime_factors(x):
            factors = {}
            for p in primes:
                if p*p > x:
                    break
                count = 0
                while x % p == 0:
                    x //= p
                    count += 1
                if count > 0:
                    factors[p] = count
            if x > 1:
                factors[x] = 1
            return factors

        fact = [1] * (n + 101)
        inv_fact = [1] * (n + 101)
        for i in range(2, n + 101):
            fact[i] = fact[i-1] * i % MOD
        inv_fact[-1] = pow(fact[-1], MOD-2, MOD)
        for i in reversed(range(1, n + 100)):
            inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

        def nCr(a, b):
            if b > a or b < 0:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a-b] % MOD

        dp = [0] * (maxValue + 1)
        dp[1] = 1
        for i in range(2, maxValue + 1):
            factors = prime_factors(i)
            ways = 1
            for e in factors.values():
                ways = (ways * nCr(n-1 + e, e)) % MOD
            dp[i] = ways

        return sum(dp[1:maxValue+1]) % MOD
