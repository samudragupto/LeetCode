MOD = 10**9 + 7
MAX = 20000

fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def precompute_factorials():
    for i in range(2, MAX + 1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact[MAX] = modinv(fact[MAX], MOD)
    for i in range(MAX-1, 0, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def nCr(n, r):
    if r > n or r < 0:
        return 0
    return (fact[n] * inv_fact[r] % MOD) * inv_fact[n-r] % MOD

def prime_factorization(k):
    factors = {}
    d = 2
    while d * d <= k:
        while k % d == 0:
            factors[d] = factors.get(d, 0) + 1
            k //= d
        d += 1
    if k > 1:
        factors[k] = factors.get(k, 0) + 1
    return factors

class Solution:
    def waysToFillArray(self, queries):
        precompute_factorials()
        result = []
        for n, k in queries:
            factors = prime_factorization(k)
            ways = 1
            for e in factors.values():
                ways = (ways * nCr(n + e - 1, e)) % MOD
            result.append(ways)
        return result
